from django.shortcuts import render
import math


def layout(request):
    context = dict()
    if request.method == 'POST':
        context['is_post'] = True
        p_od = float(request.POST['p_od'])
        p_t = float(request.POST['p_t'])
        p_d = float(request.POST['p_d'])
        # p_c = float(request.POST['p_c'])
        thickness = float(request.POST['thickness'])
        density = float(request.POST['density'])
        air = float(request.POST['air'])
        # water = float(request.POST['water'])
        sea_water = float(request.POST['sea_water'])
        pipe_inside_radious = (p_od - (2*p_t)) / 2
        pipe_outside_radious = (p_od / 2)
        outer_radious_of_coating = (p_od / 2) + (thickness / 2)
        pipe_weight = (((math.pi) * ((pipe_outside_radious*pipe_outside_radious)-(pipe_inside_radious*pipe_inside_radious))) / 144) * p_d
        coating_weight = (((math.pi) * ((outer_radious_of_coating*outer_radious_of_coating)-(pipe_outside_radious*pipe_outside_radious))) / 144) * density
        contents_weight = (((math.pi) * (pipe_inside_radious*pipe_inside_radious)) / 144) * air
        total_weight = pipe_weight + coating_weight + contents_weight
        buoyant_force = (((math.pi) * (outer_radious_of_coating*outer_radious_of_coating)) / 144) * sea_water
        data = {
            'pipe_inside_radious': pipe_inside_radious,
            'pipe_outside_radious': pipe_outside_radious,
            'outer_radious_of_coating': outer_radious_of_coating,
            'total_pipeline': 2 * ((p_od / 2) + (thickness / 2)),
            'pipe_weight': pipe_weight,
            'coating_weight': coating_weight,
            'contents_weight': contents_weight,
            'total_weight': total_weight,
            'buoyant_force': buoyant_force,
            'submergerd_weight': total_weight - buoyant_force,
            'submergerd_gravity': total_weight / buoyant_force,
        }
        context['data'] = data
    return render(request, 'submergedWeight/layout.html', context)
