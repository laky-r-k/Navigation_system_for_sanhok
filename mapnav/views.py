from django.shortcuts import render
import subprocess
from django.http import HttpResponse



def map_view(request):
    return render(request, "mapnav/map.html")


def find_path(request):
    start = request.GET.get("start")
    end = request.GET.get("end")
    
    if not start or not end:
        return HttpResponse("Invalid input.", status=400)

    try:
        result = subprocess.run(
            ["mapnav/dijkstra/dijkstra.exe", start, end],
            capture_output=True,
            text=True
        )
        print("=== Dijkstra stdout ===")
        print(result.stdout)
        print("=== Dijkstra stderr ===")
        print(result.stderr)
        
        return HttpResponse(result.stdout)
    except Exception as e:
        print("=== Exception occurred ===")
        print(str(e))
        return HttpResponse("Error running Dijkstra", status=500)

