class Settings:

    def __init__(self):
        """initializes the games settings"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (40,130,230)

        #ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1