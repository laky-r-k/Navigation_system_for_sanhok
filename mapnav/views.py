from django.shortcuts import render
import subprocess
from django.http import JsonResponse, HttpResponse
from .models import Road
import re
import os
import json
def map_view(request):
    return render(request, "mapnav/map.html")


def find_path(request):
    # Get start and end from query parameters
    start = request.GET.get("start")
    end = request.GET.get("end")

    if not start or not end:
        return HttpResponse("Invalid input.", status=400)

    try:
        # Run Dijkstra executable
        result = subprocess.run(
            ["mapnav/dijkstra/dijkstra.exe", start, end],
            capture_output=True,
            text=True
        )

        print("=== Dijkstra stdout ===")
        print(result.stdout)
        print("=== Dijkstra stderr ===")
        print(result.stderr)

        # Extract path line (assume it contains '->')
        path_line = next((line for line in result.stdout.splitlines() if '->' in line), '')
        nodes = re.findall(r'[A-Za-z_]+', path_line)
        nodes.pop(0)
        nodes.pop(0)

        if len(nodes) < 2:
            return JsonResponse({'error': 'No path found or invalid output'}, status=404)

        # Load road data from JSON file
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        road_json_path = os.path.join(BASE_DIR, "mapnav", "data", "road_data.json")

        try:
            with open(road_json_path, 'r') as f:
                road_data = json.load(f)
        except Exception as e:
            print(f"Error reading JSON: {e}")
            return JsonResponse({'error': 'Failed to read road data'}, status=500)

        route_segments = []

        for i in range(len(nodes) - 1):
            s = nodes[i]
            e = nodes[i + 1]

            # Try to find the matching road segment in either direction
            segment = next((r for r in road_data if (r['start_node'] == s and r['end_node'] == e) or (r['start_node'] == e and r['end_node'] == s)), None)

            if not segment:
                return JsonResponse({'error': f'Road segment missing between {s} and {e}'}, status=404)

            route_segments.append({
                'start_node': segment['start_node'],
                'end_node': segment['end_node'],
                'polyline': segment['polyline'],
            })
        
        return JsonResponse({'route': route_segments})

    except Exception as e:
        print("=== Exception occurred ===")
        print(str(e))
        return HttpResponse("Error running Dijkstra", status=500)
