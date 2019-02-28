import module_arene as arene
import module_robot as robot
import module_affichage as affichage

test_r = robot.Robot(500, 500, 100, 100)
test_a = arene.Arene(1000, test_r)
test_f = affichage.AffichageTK(test_a, test_r)






