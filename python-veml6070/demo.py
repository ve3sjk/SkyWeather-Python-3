#!/usr/bin/env python
import sys
import veml6070
sys.path.append('./SDL_Pi_TCA9545')

import SDL_Pi_TCA9545


################
# TCA9545 I2C Mux 

#/*=========================================================================
#    I2C ADDRESS/BITS
#    -----------------------------------------------------------------------*/
TCA9545_ADDRESS =                         (0x73)    # 1110011 (A0+A1=VDD)
#/*=========================================================================*/

#/*=========================================================================
#    CONFIG REGISTER (R/W)
#    -----------------------------------------------------------------------*/
TCA9545_REG_CONFIG            =          (0x00)
#    /*---------------------------------------------------------------------*/

TCA9545_CONFIG_BUS0  =                (0x01)  # 1 = enable, 0 = disable 
TCA9545_CONFIG_BUS1  =                (0x02)  # 1 = enable, 0 = disable 
TCA9545_CONFIG_BUS2  =                (0x04)  # 1 = enable, 0 = disable 
TCA9545_CONFIG_BUS3  =                (0x08)  # 1 = enable, 0 = disable 

#/*=========================================================================*/

# I2C Mux TCA9545 Detection
try:
	tca9545 = SDL_Pi_TCA9545.SDL_Pi_TCA9545(addr=TCA9545_ADDRESS, bus_enable = TCA9545_CONFIG_BUS0)


	# turn I2CBus 3 on
	tca9545.write_control_register(TCA9545_CONFIG_BUS3)
	print ">>>>>>>>>>>>>>>>>>><<<<<<<<<<<"
	print "TCA9545 I2C Mux Not Present" 
	print ">>>>>>>>>>>>>>>>>>><<<<<<<<<<<"
	# config.TCA9545_I2CMux_Present = True
except:
	print ">>>>>>>>>>>>>>>>>>><<<<<<<<<<<"
	print "TCA9545 I2C Mux Not Present" 
	print ">>>>>>>>>>>>>>>>>>><<<<<<<<<<<"
	# config.TCA9545_I2CMux_Present = False
	
def get_estimated_risk_level(intensity):
    """
    returns estimated risk level from comparing UVA light intensity value
    in W/(m*m) as parameter, thresholds calculated from application notes
    """
    if intensity < 24.888:
		return "low"
    if intensity < 49.800:
        return "moderate"
    if intensity < 66.400:
        return "high"
    if intensity < 91.288:
        return "very high"
    return "extreme"


ALL_INTEGRATION_TIMES = [
    veml6070.INTEGRATIONTIME_1_2T, veml6070.INTEGRATIONTIME_1T, veml6070.INTEGRATIONTIME_2T, veml6070.INTEGRATIONTIME_4T
]

if __name__ == '__main__':
    veml = veml6070.Veml6070()
    for i in ALL_INTEGRATION_TIMES:
        veml.set_integration_time(i)
        uv_raw = veml.get_uva_light_intensity_raw()
        uv = veml.get_uva_light_intensity()
        uvi = get_estimated_risk_level(uv)
        print("Integration Time setting %d: %f W/(m*m) from raw value %d give uvi value of %s" % (i, uv, uv_raw, uvi))


