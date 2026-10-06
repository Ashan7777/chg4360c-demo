class Bioreactor:
    def __init__(self, process_name, ph_lims, ph_chg, temp_lims, temp_chg):
       self.process_name = process_name
       self.ph_min = ph_lims[0]
       self.ph_max = ph_lims[1]
       self.ph_chg = ph_chg
       self.temp_min = temp_lims[0]
       self.temp_max = temp_lims[1]
       self.temp_chg = temp_chg

    def in_optimal_range(self, ph, temperature):
        ph_ok = (self.ph_min <= ph <= self.ph_max)
        temperature_ok = (self.temp_min <= temperature <= self.temp_max)
        process_ok = (ph_ok and temperature_ok)
        print(f"===== ({ph = :.2f}) ==== (T={temperature:.2f}) =====")

        return process_ok

    def simulate_process(self, initial_ph, initial_temp):
        print(f"\n================== {self.process_name} CONTROL START ==================")
        # intial pH and temperature
        ph = initial_ph
        temperature = initial_temp

        process_ok = self.in_optimal_range(ph, temperature)

        while not process_ok:
            if ph > self.ph_max:
                print("pH is too high. Injecting Acid...")
                ph -= self.ph_chg
            elif ph < self.ph_min:
                print("pH is too low. Injecting Base...")
                ph += self.ph_chg
            else:
                print("pH is ok.")

            if temperature > self.temp_max:
                print("Temperature is too high. Increase cooling water flow rate...")
                temperature -= self.temp_chg
            elif temperature < self.temp_min:
                print("Temperature is too low. Decrease cooling water flow rate...")
                temperature += self.temp_chg
            else:
                print("Temperature is ok.")

            process_ok = self.in_optimal_range(ph, temperature)

        print(f"\n================== {self.process_name} CONTROL END ==================")

# MAIN CODE

bioreactor_1 = Bioreactor(process_name="Ethanol fermentation", ph_lims=[4.0,5.0], ph_chg= 0.1, temp_lims=[28,32], temp_chg = 0.4)

bioreactor_2 = Bioreactor(process_name="Thermophilic anaerobic digestion", ph_lims=[6.8,7.8], ph_chg= 0.1, temp_lims=[50,60], temp_chg = 0.8)

# RUN SIMULATIONS
bioreactor_1.simulate_process(initial_ph=5.15, initial_temp=26.1)
bioreactor_2.simulate_process(initial_ph=6.35, initial_temp=62.2)