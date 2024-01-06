"""Energy module for the simulation
"""

import math


class Energy:
    """Energy class
    This class is used to calculate the energy consumption of the vehicle.

    Attributes:
        mass: The mass of the vehicle. (unit: kg)
        coeff_mass_factor: The mass factor of the vehicle.
        acceleration: The acceleration of the vehicle. (unit: m^2 / s)
        coeff_roll_r: The coefficient of rolling resistance.
        air_density: The air density of the environment. (unit: kg/m^3)
        front_area: The front area of the vehicle. (unit: m^2)
        coeff_aero_drag: The aerodynamic drag coefficient.
        wind_speed: The wind speed of the environment. (unit: m/s)
        road_angle: The angle of the road. (unit: degree)
    """

    def __init__(self):
        # Group 0: constants
        self.GRAV_ACC: float = 9.8  # Gravitational Acceleration (unit: m/s^2)

        # Group 1: vehicle parameters
        self.mass: float = 2000  # Unit: kg
        self.mass_factor: float = 1.05  # Mass factor coefficient
        self.acceleration: float = 0  # Unit: m^2 / s
        self.roll_r: float = 0.02  # Rolling resistance coefficient
        self.driving_speed: float = 0  # Unit: m/s

        # Group 2: environment parameters
        self.air_density: float = 1.225  # Unit: kg/m^3
        self.front_area: float = 2  # Unit: m^2
        self.aero_drag: float = 0.5  # Aerodynamic drag coefficient
        self.wind_speed: float = 0  # Unit: m/s

        # Group 3: road parameters
        self.road_angle: float = 0  # angle

    def calculate(self, road_angle: float, driving_speed: float) -> float:
        """Calculate the energy consumption of the vehicle
        in a given road condition.

        Args:
            road_angle (float): the angle of the road (unit: degree)
            driving_speed (float): the driving speed of the vehicle (unit: m/s)

        Returns:
            float: the energy consumption of the vehicle
        """

        # Step 1: set up attributes
        self.driving_speed: float = driving_speed
        self.road_angle: float = road_angle

        # Step 2: calculate assistant parameters
        raw_radian: float = math.radians(self.road_angle)
        cos_radian: float = math.cos(raw_radian)
        sin_radian: float = math.sin(raw_radian)

        # Step 2: calculate basic energy consumption parameters
        p1: float = (
            self.mass_factor * self.mass * self.acceleration +
            self.mass * self.GRAV_ACC * self.roll_r * cos_radian
        )
        p2: float = (
            0.5 * self.air_density * self.front_area * self.aero_drag *
            (self.driving_speed - self.wind_speed) ** 2
        )
        p3: float = self.mass * self.GRAV_ACC * sin_radian

        # Step 3: calculate the overall energy consumption
        return (p1 + p2 + p3) * self.driving_speed   # Unit: Watt
