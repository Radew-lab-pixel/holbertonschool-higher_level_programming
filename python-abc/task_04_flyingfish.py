#!/usr/bin/python3
"""multiple inheritance FlyingFish inherits from Fish and Bird"""

class Fish:
    """parent class Fish"""
    def swim(self):
        """method swim"""
        print(f"The fish is swimming")

    def habitat(self):
        """method habitat"""
        print(f"The fish lives in water")

class Bird:
    """parent class Bird"""
    def fly(self):
        """method fly"""
        print(f"The bird is flying")

    def habitat(self):
        """method habitat"""
        print(f"The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """child class FlyingFish"""
    def swim(self):
        """method swim"""
        print(f"The flying fish is swimming")

    def habitat(self):
        """method habitat"""
        print(f"The flying fish lives both in water and the sky")

    def fly(self):
        """method fly"""
        print(f"The flying fish is soaring")
