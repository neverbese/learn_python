from robot.models import robot 


def talk():
    restautrant_robot = robot.RestaurantRobot()
    restautrant_robot.hello()
    restautrant_robot.recommend_restaurant()
    restautrant_robot.ask_user_favorite()
    restautrant_robot.thank_you()