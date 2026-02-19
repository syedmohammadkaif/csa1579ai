planet(mercury, rocky, small, hot, closest_to_sun).
planet(venus, rocky, small, hot,second_closest_to_sun).
planet(earth, rocky, medium, temperature, third_closest_to_sun).
planet(mars, rocky, small, cold, forth_closest_to_sun).
planet(jupiter, gas_gaint, large, cold, fifth_closest_to_sun).
planet(saturn, gas_gaint, large, cold, sisth_closest_to_sun).
palnet(uranus, ice_gaint, large, cold, seventh_closest_to_sun).
planet(neptune, ice_gaint,  large, cold, eighth_closest_to_sun).

planet_properties(Name, Type, Size, Temperature, Position):-
    planet(Name, Type, Size,  Temperature, Position).

