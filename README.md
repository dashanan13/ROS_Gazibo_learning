This repository is dedicated to a project aimed at improvement of "SnakeSIM: a ROS-based Rapid-Prototyping Framework for Perception-Driven Obstacle-Aided Locomotion of Snake Robots" by Filippo Sanfilippo, Øyvind Stavdahl and Pal Liljeb.
Paper link: 
https://filipposanfilippo.inspitivity.com/publications/sanfilippo-snakesim-a-ros-based-rapid-prototyping-framework-for-perception-driven-obstacle-aided-locomotion-of-snake-robots.pdf
https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/2494074

The following assumptions are considered in the paper and one of these assumptions will be aimed for improvement:
1) a path, S(s), with s being the path length parameter, is known. The obstacle locations, o1, o2, o3, are also known;
2) the snake is always on the path S(s);
3) the snake is planar and discrete (joints and links are numbered from left to right);
4) there is no ground or obstacle friction;
5) the snake is at rest;
6) the snake tail link is tethered to the ground, as shown in Fig. 5. The tether is unactuated. No tangential movements are allowed. The tail is not restricted in any other way. A tensile force, fs, acts along the tangent at o1. Note that, the only reason why the tether is introduced is to justify a static analysis – which is of course an approximation of the real case;
7) the snake is perfectly rigid except at the point where an internal torque can be applied. The obstacles are perfectly rigid and fixed to the ground surface;
8) we choose to apply an internal torque, t, at a known point, p23, on the path between o2 and o3, as shown in Fig. 5.
