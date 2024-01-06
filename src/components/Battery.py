"""Battery module for the simulation
"""


class Battery:
    """Lithium ion battery class

    Attributes:
        capacity (TYPE): Description
        cell_voltage (TYPE): Description
        cutoff_voltage (TYPE): Description
        energy_consume (TYPE): Description
        grade (TYPE): Description
        need_charge (TYPE): Description
        output (TYPE): Description
        SOC (TYPE): Description
        total_capacity (TYPE): Description

    Remarks:
        working voltage: 3.8
        cut-off voltage: 2
        cell counts: 100
    """

    def __init__(self, capacity: float):
        self.cell_voltage: float = 4
        self.cutoff_voltage: float = 2
        self.grade: float = (self.cell_voltage - self.cutoff_voltage) / 100
        self.total_capacity: float = capacity
        self.capacity: float = capacity  # Unit: Wh
        self.Ah: float = self.capacity / (self.cell_voltage * 100)
        self.need_charge: bool = False
        self.energy_consume: float = 0
        self.soc: float = 0.9

    def use(self, duration: float, power: float) -> bool:
        """Use battery for a duration with a power

        Args:
            duration (float): the duration of using battery (unit: second)
            power (float): the power of using battery (unit: Watt)

        Returns:
            bool: whether the battery need to be charged
        """

        # Step 1: calculate the SOC
        self.soc = self.capacity / self.total_capacity

        if self.soc > 0.9:
            self.soc = 0.9
        if self.soc <= 0.2:
            self.need_charge = True

        self.cell_voltage = (
            self.soc * 100 * self.grade +
            self.cutoff_voltage
        )

        # Step 2: calculate the energy consumed
        if not self.need_charge:
            self.energy_consume = duration * power / (3600)
            self.capacity -= duration * power / (3600)

        return self.need_charge

    def charge(self, wh: float) -> None:
        """charge the battery with a energy (unit: Wh)

        Args:
            wh (float): the energy that the battery charged (unit: Wh)
        """

        if (wh + self.capacity) > self.total_capacity:
            self.capacity = self.total_capacity
            self.need_charge = False
        else:
            self.capacity = wh + self.capacity
            self.need_charge = False
