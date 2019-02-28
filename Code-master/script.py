import module_arene as arene
import module_robot as robot
import module_affichage as affichage

robot=robot.Robot(500, 500, 50, 50)
arene=arene.Arene(700, robot)

canvas=affichage.AffichageTK(arene,robot)


#point=[(30,30),(40,600), (600,40), (300,300), (40,600), (600,40), (600,200)]


print(canvas.robot.ptv)
canvas.robot.rotation(90)
print(canvas.robot.ptv)







