conversion_factors = {
    # Length conversions
    ("Meters", "Kilometers"): 0.001,
    ("Kilometers", "Meters"): 1000,
    ("Meters", "Centimeters"): 100,
    ("Centimeters", "Meters"): 0.01,
    ("Meters", "Millimeters"): 1000,
    ("Millimeters", "Meters"): 0.001,
    ("Kilometers", "Centimeters"): 100000,  # Added
    ("Centimeters", "Kilometers"): 0.00001,  # Added
    ("Miles", "Kilometers"): 1.60934,
    ("Kilometers", "Miles"): 0.621371,
    ("Yards", "Meters"): 0.9144,
    ("Meters", "Yards"): 1.09361,
    ("Feet", "Meters"): 0.3048,
    ("Meters", "Feet"): 3.28084,
    ("Meters", "Inches"): 39.3701,
    ("Inches", "Meters"): 0.0254,
    ("Kilometers", "Yards"): 1093.61,
    ("Yards", "Kilometers"): 0.0009144,
    ("Kilometers", "Feet"): 3280.84,
    ("Feet", "Kilometers"): 0.0003048,
    ("Kilometers", "Inches"): 39370.1,
    ("Inches", "Kilometers"): 0.0000254,
    ("Centimeters", "Millimeters"): 10,
    ("Millimeters", "Centimeters"): 0.1,
    ("Feet", "Inches"): 12,
    ("Inches", "Feet"): 1/12,
    ("Yards", "Feet"): 3,
    ("Feet", "Yards"): 1/3,
    ("Inches", "Yards"): 0.0277778,
    ("Yards", "Inches"): 36,
    ("Inches", "Miles"): 1.5783e-5,
    ("Miles", "Inches"): 63360,
    ("Meters", "Miles"): 0.000621371,
    ("Miles", "Meters"): 1609.34,
    ("Kilometers", "Millimeters"): 1_000_000,
("Millimeters", "Kilometers"): 0.000001,
("Centimeters", "Miles"): 6.2137e-6,
("Miles", "Centimeters"): 160934,
("Centimeters", "Yards"): 0.0109361,
("Yards", "Centimeters"): 91.44,
("Centimeters", "Feet"): 0.0328084,
("Feet", "Centimeters"): 30.48,
("Centimeters", "Inches"): 0.393701,
("Inches", "Centimeters"): 2.54,
("Millimeters", "Miles"): 6.2137e-7,
("Miles", "Millimeters"): 1609344,
("Millimeters", "Yards"): 0.00109361,
("Yards", "Millimeters"): 914.4,
("Millimeters", "Feet"): 0.00328084,
("Feet", "Millimeters"): 304.8,
("Millimeters", "Inches"): 0.0393701,
("Inches", "Millimeters"): 25.4,
("Miles", "Yards"): 1760,
("Yards", "Miles"): 1/1760,
("Miles", "Feet"): 5280,
("Feet", "Miles"): 1/5280,
("Miles", "Inches"): 63360,
("Inches", "Miles"): 1/63360,
("Grams", "Kilograms"): 0.001,
("Kilograms", "Grams"): 1000,
("Grams", "Pounds"): 0.00220462,
("Pounds", "Grams"): 453.592,
("Grams", "Ounces"): 0.035274,
("Ounces", "Grams"): 28.3495,
("Kilograms", "Pounds"): 2.20462,
("Pounds", "Kilograms"): 0.453592,
("Kilograms", "Ounces"): 35.274,
("Ounces", "Kilograms"): 0.0283495,
("Pounds", "Ounces"): 16,
("Ounces", "Pounds"): 1/16,
    ("Nautical Miles", "Meters"): 1852,
    ("Meters", "Nautical Miles"): 0.000539957,
    ("Nautical Miles", "Kilometers"): 1.852,
    ("Kilometers", "Nautical Miles"): 0.539957,
    ("Nautical Miles", "Miles"): 1.15078,
    ("Miles", "Nautical Miles"): 0.868976,
    ("Nautical Miles", "Yards"): 2025.37,
    ("Yards", "Nautical Miles"): 0.000493737,
    ("Nautical Miles", "Feet"): 6076.12,
    ("Feet", "Nautical Miles"): 0.000164579,
    ("Nautical Miles", "Inches"): 72913.4,
    ("Inches", "Nautical Miles"): 1.3715e-5,
    ("Nautical Miles", "Millimeters"): 1_852_000,
    ("Millimeters", "Nautical Miles"): 5.39957e-7,
    ("Nautical Miles", "Centimeters"): 185_200,
    ("Centimeters", "Nautical Miles"): 5.39957e-6,

    # Light Years
    ("Light Years", "Meters"): 9.461e15,
    ("Meters", "Light Years"): 1.057e-16,
    ("Light Years", "Kilometers"): 9.461e12,
    ("Kilometers", "Light Years"): 1.057e-13,
    ("Light Years", "Miles"): 5.878e12,
    ("Miles", "Light Years"): 1.701e-13,
    ("Light Years", "Yards"): 6.451e15,
    ("Yards", "Light Years"): 1.55e-16,
    ("Light Years", "Feet"): 1.936e16,
    ("Feet", "Light Years"): 5.096e-17,
    ("Light Years", "Inches"): 2.323e17,
    ("Inches", "Light Years"): 4.3e-18,
    ("Light Years", "Millimeters"): 9.461e18,
    ("Millimeters", "Light Years"): 1.057e-19,
    ("Light Years", "Centimeters"): 9.461e17,
    ("Centimeters", "Light Years"): 1.057e-18,

    # Micrometers & Nanometers
    ("Meters", "Micrometers"): 1_000_000,
    ("Micrometers", "Meters"): 1e-6,
    ("Meters", "Nanometers"): 1_000_000_000,
    ("Nanometers", "Meters"): 1e-9,
    ("Kilometers", "Micrometers"): 1_000_000_000,
    ("Micrometers", "Kilometers"): 1e-9,
    ("Kilometers", "Nanometers"): 1_000_000_000_000,
    ("Nanometers", "Kilometers"): 1e-12,
    ("Miles", "Micrometers"): 1.609e9,
    ("Micrometers", "Miles"): 6.214e-10,
    ("Miles", "Nanometers"): 1.609e12,
    ("Nanometers", "Miles"): 6.214e-13,
    ("Yards", "Micrometers"): 914400,
    ("Micrometers", "Yards"): 1.094e-6,
    ("Yards", "Nanometers"): 914400000,
    ("Nanometers", "Yards"): 1.094e-9,
    ("Feet", "Micrometers"): 304800,
    ("Micrometers", "Feet"): 3.281e-6,
    ("Feet", "Nanometers"): 304800000,
    ("Nanometers", "Feet"): 3.281e-9,
    ("Inches", "Micrometers"): 25400,
    ("Micrometers", "Inches"): 3.937e-5,
    ("Inches", "Nanometers"): 25400000,
    ("Nanometers", "Inches"): 3.937e-8,

    # General length conversions
    ("Meters", "Kilometers"): 0.001,
    ("Kilometers", "Meters"): 1000,
    ("Meters", "Centimeters"): 100,
    ("Centimeters", "Meters"): 0.01,
    ("Meters", "Millimeters"): 1000,
    ("Millimeters", "Meters"): 0.001,
    ("Miles", "Kilometers"): 1.60934,
    ("Kilometers", "Miles"): 0.621371,
    ("Yards", "Meters"): 0.9144,
    ("Meters", "Yards"): 1.09361,
    ("Feet", "Meters"): 0.3048,
    ("Meters", "Feet"): 3.28084,
    ("Meters", "Inches"): 39.3701,
    ("Inches", "Meters"): 0.0254,
    ("Kilometers", "Yards"): 1093.61,
    ("Yards", "Kilometers"): 0.0009144,
    ("Kilometers", "Feet"): 3280.84,
    ("Feet", "Kilometers"): 0.0003048,
    ("Kilometers", "Inches"): 39370.1,
    ("Inches", "Kilometers"): 0.0000254,
    ("Centimeters", "Millimeters"): 10,
    ("Millimeters", "Centimeters"): 0.1,
    ("Feet", "Inches"): 12,
    ("Inches", "Feet"): 1/12,
    ("Yards", "Feet"): 3,
    ("Feet", "Yards"): 1/3,
    ("Inches", "Yards"): 0.0277778,
    ("Yards", "Inches"): 36,
    ("Inches", "Miles"): 1.5783e-5,
    ("Miles", "Inches"): 63360,
    ("Meters", "Miles"): 0.000621371,
    ("Miles", "Meters"): 1609.34,
 ("Nautical Miles", "Light Years"): 9.8747e-13,
    ("Light Years", "Nautical Miles"): 1.01265e12,
    ("Nautical Miles", "Micrometers"): 1.852e9,
    ("Micrometers", "Nautical Miles"): 5.39957e-10,
    ("Nautical Miles", "Nanometers"): 1.852e12,
    ("Nanometers", "Nautical Miles"): 5.39957e-13,
    ("Light Years", "Micrometers"): 9.461e21,
    ("Micrometers", "Light Years"): 1.057e-22,
    ("Light Years", "Nanometers"): 9.461e24,
    ("Nanometers", "Light Years"): 1.057e-25,
 ("Micrometers", "Millimeters"): 0.001,
    ("Millimeters", "Micrometers"): 1000,
    ("Micrometers", "Centimeters"): 0.0001,
    ("Centimeters", "Micrometers"): 10000,
    ("Micrometers", "Meters"): 1e-6,
    ("Meters", "Micrometers"): 1e6,
    ("Micrometers", "Kilometers"): 1e-9,
    ("Kilometers", "Micrometers"): 1e9,
    ("Micrometers", "Inches"): 3.93701e-5,
    ("Inches", "Micrometers"): 25400,
    ("Micrometers", "Feet"): 3.28084e-6,
    ("Feet", "Micrometers"): 304800,
    ("Micrometers", "Yards"): 1.09361e-6,
    ("Yards", "Micrometers"): 914400,
    ("Micrometers", "Miles"): 6.21371e-10,
    ("Miles", "Micrometers"): 1.60934e9,

    # Nanometers to other units
    ("Nanometers", "Micrometers"): 0.001,
    ("Micrometers", "Nanometers"): 1000,
    ("Nanometers", "Millimeters"): 1e-6,
    ("Millimeters", "Nanometers"): 1e6,
    ("Nanometers", "Centimeters"): 1e-7,
    ("Centimeters", "Nanometers"): 1e7,
    ("Nanometers", "Meters"): 1e-9,
    ("Meters", "Nanometers"): 1e9,
    ("Nanometers", "Kilometers"): 1e-12,
    ("Kilometers", "Nanometers"): 1e12,
    ("Nanometers", "Inches"): 3.93701e-8,
    ("Inches", "Nanometers"): 2.54e7,
    ("Nanometers", "Feet"): 3.28084e-9,
    ("Feet", "Nanometers"): 3.048e8,
    ("Nanometers", "Yards"): 1.09361e-9,
    ("Yards", "Nanometers"): 9.144e8,
    ("Nanometers", "Miles"): 6.21371e-13,
    ("Miles", "Nanometers"): 1.60934e12,
        ("Milligrams", "Grams"): 0.001,
    ("Grams", "Milligrams"): 1000,
    ("Milligrams", "Kilograms"): 1e-6,
    ("Kilograms", "Milligrams"): 1e6,
    ("Milligrams", "Metric Tons"): 1e-9,
    ("Metric Tons", "Milligrams"): 1e9,
    ("Milligrams", "Pounds"): 2.20462e-6,
    ("Pounds", "Milligrams"): 453592,
    ("Milligrams", "Ounces"): 3.5274e-5,
    ("Ounces", "Milligrams"): 28349.5,

    # Grams to other units
    ("Grams", "Kilograms"): 0.001,
    ("Kilograms", "Grams"): 1000,
    ("Grams", "Metric Tons"): 1e-6,
    ("Metric Tons", "Grams"): 1e6,
    ("Grams", "Pounds"): 0.00220462,
    ("Pounds", "Grams"): 453.592,
    ("Grams", "Ounces"): 0.035274,
    ("Ounces", "Grams"): 28.3495,
    ("Grams", "Carats"): 5,
    ("Carats", "Grams"): 0.2,
    ("Grams", "Grains"): 15.4324,
    ("Grains", "Grams"): 0.0647989,

    # Kilograms to other units
    ("Kilograms", "Metric Tons"): 0.001,
    ("Metric Tons", "Kilograms"): 1000,
    ("Kilograms", "Pounds"): 2.20462,
    ("Pounds", "Kilograms"): 0.453592,
    ("Kilograms", "Ounces"): 35.274,
    ("Ounces", "Kilograms"): 0.0283495,
    ("Kilograms", "Stones"): 0.157473,
    ("Stones", "Kilograms"): 6.35029,
    ("Kilograms", "Long Tons (UK)"): 0.000984207,
    ("Long Tons (UK)", "Kilograms"): 1016.05,
    ("Kilograms", "Short Tons (US)"): 0.00110231,
    ("Short Tons (US)", "Kilograms"): 907.185,

    # Pounds to other units
    ("Pounds", "Ounces"): 16,
    ("Ounces", "Pounds"): 1/16,
    ("Pounds", "Stones"): 1/14,
    ("Stones", "Pounds"): 14,
    ("Pounds", "Grains"): 7000,
    ("Grains", "Pounds"): 1/7000,
    ("Pounds", "Metric Tons"): 0.000453592,
    ("Metric Tons", "Pounds"): 2204.62,
    ("Pounds", "Long Tons (UK)"): 1/2240,
    ("Long Tons (UK)", "Pounds"): 2240,
    ("Pounds", "Short Tons (US)"): 1/2000,
    ("Short Tons (US)", "Pounds"): 2000,

    # Metric Tons to other units
    ("Metric Tons", "Long Tons (UK)"): 0.984207,
    ("Long Tons (UK)", "Metric Tons"): 1.01605,
    ("Metric Tons", "Short Tons (US)"): 1.10231,
    ("Short Tons (US)", "Metric Tons"): 0.907185,
        ("Milligrams", "Stones"): 6.35029e-8,
    ("Stones", "Milligrams"): 1.57473e7,

    # Milligrams to other units
    ("Milligrams", "Grams"): 0.001,
    ("Grams", "Milligrams"): 1000,
    ("Milligrams", "Kilograms"): 1e-6,
    ("Kilograms", "Milligrams"): 1e6,
    ("Milligrams", "Metric Tons"): 1e-9,
    ("Metric Tons", "Milligrams"): 1e9,
    ("Milligrams", "Pounds"): 2.20462e-6,
    ("Pounds", "Milligrams"): 453592,
    ("Milligrams", "Ounces"): 3.5274e-5,
    ("Ounces", "Milligrams"): 28349.5,

    # Grams to other units
    ("Grams", "Kilograms"): 0.001,
    ("Kilograms", "Grams"): 1000,
    ("Grams", "Metric Tons"): 1e-6,
    ("Metric Tons", "Grams"): 1e6,
    ("Grams", "Pounds"): 0.00220462,
    ("Pounds", "Grams"): 453.592,
    ("Grams", "Ounces"): 0.035274,
    ("Ounces", "Grams"): 28.3495,
    ("Grams", "Carats"): 5,
    ("Carats", "Grams"): 0.2,
    ("Grams", "Grains"): 15.4324,
    ("Grains", "Grams"): 0.0647989,

    # Kilograms to other units
    ("Kilograms", "Metric Tons"): 0.001,
    ("Metric Tons", "Kilograms"): 1000,
    ("Kilograms", "Pounds"): 2.20462,
    ("Pounds", "Kilograms"): 0.453592,
    ("Kilograms", "Ounces"): 35.274,
    ("Ounces", "Kilograms"): 0.0283495,
    ("Kilograms", "Stones"): 0.157473,
    ("Stones", "Kilograms"): 6.35029,
    ("Kilograms", "Long Tons (UK)"): 0.000984207,
    ("Long Tons (UK)", "Kilograms"): 1016.05,
    ("Kilograms", "Short Tons (US)"): 0.00110231,
    ("Short Tons (US)", "Kilograms"): 907.185,

    # Pounds to other units
    ("Pounds", "Ounces"): 16,
    ("Ounces", "Pounds"): 1/16,
    ("Pounds", "Stones"): 1/14,
    ("Stones", "Pounds"): 14,
    ("Pounds", "Grains"): 7000,
    ("Grains", "Pounds"): 1/7000,
    ("Pounds", "Metric Tons"): 0.000453592,
    ("Metric Tons", "Pounds"): 2204.62,
    ("Pounds", "Long Tons (UK)"): 1/2240,
    ("Long Tons (UK)", "Pounds"): 2240,
    ("Pounds", "Short Tons (US)"): 1/2000,
    ("Short Tons (US)", "Pounds"): 2000,

    # Metric Tons to other units
    ("Metric Tons", "Long Tons (UK)"): 0.984207,
    ("Long Tons (UK)", "Metric Tons"): 1.01605,
    ("Metric Tons", "Short Tons (US)"): 1.10231,
    ("Short Tons (US)", "Metric Tons"): 0.907185,
        ("Milligrams", "Carats"): 0.005,
    ("Carats", "Milligrams"): 200,
        ("Milligrams", "Grains"): 0.0154324,
    ("Grains", "Milligrams"): 64.7989,
        ("Milligrams", "Long Tons (UK)"): 9.8421e-10,
    ("Long Tons (UK)", "Milligrams"): 1.01605e9,
        ("Milligrams", "Short Tons (US)"): 1.1023e-9,
    ("Short Tons (US)", "Milligrams"): 9.07185e8,
    # Grams to Short Tons (US)
    ("Grams", "Short Tons (US)"): 1.1023e-6,
    ("Short Tons (US)", "Grams"): 907184.74,

    # Grams to Long Tons (UK)
    ("Grams", "Long Tons (UK)"): 9.8421e-7,
    ("Long Tons (UK)", "Grams"): 1.016e6,

    # Grams to Stones
    ("Grams", "Stones"): 0.000157473,
    ("Stones", "Grams"): 6350.29,
    # Kilograms to Carats
    ("Kilograms", "Carats"): 5000,
    ("Carats", "Kilograms"): 0.0002,

    # Kilograms to Grains
    ("Kilograms", "Grains"): 15432.3584,
    ("Grains", "Kilograms"): 6.47989e-5,
    # Metric Tons to Ounces
    ("Metric Tons", "Ounces"): 35273.9619,
    ("Ounces", "Metric Tons"): 2.835e-5,

    # Metric Tons to Stones
    ("Metric Tons", "Stones"): 157.473,
    ("Stones", "Metric Tons"): 0.00635,

    # Metric Tons to Carats
    ("Metric Tons", "Carats"): 5000000,
    ("Carats", "Metric Tons"): 2e-7,

    # Metric Tons to Grains
    ("Metric Tons", "Grains"): 15432358.4,
    ("Grains", "Metric Tons"): 6.47989e-8,
    ("Pounds", "Carats"): 2267.96,  # 1 Pound = 2267.96 Carats
("Carats", "Pounds"): 0.00044,  # 1 Carat = 0.00044 Pounds
("Ounces", "Stones"): 1 / 224,
("Stones", "Ounces"): 224,
 ("Ounces", "Carats"): 141.7475,  # 1 ounce = 141.7475 carats
    ("Carats", "Ounces"): 1 / 141.7475,  # 1 carat = 0.007055 ounces

    # Ounces to Grains
    ("Ounces", "Grains"): 437.5,  # 1 ounce = 437.5 grains
    ("Grains", "Ounces"): 1 / 437.5,  # 1 grain = 0.002285 ounces

    # Ounces to Short Tons (US)
    ("Ounces", "Short Tons (US)"): 0.00003125,  # 1 ounce = 0.00003125 short tons
    ("Short Tons (US)", "Ounces"): 32000,  # 1 short ton = 32,000 ounces

    # Ounces to Long Tons (UK)
    ("Ounces", "Long Tons (UK)"): 0.0000279,  # 1 ounce = 0.0000279 long tons
    ("Long Tons (UK)", "Ounces"): 35840, 
    ("Stones", "Carats"): 31751.5,  # 1 stone = 31,751.5 carats
    ("Carats", "Stones"): 1 / 31751.5,  # 1 carat = 0.0000315 stones

    # Stones to Grains
    ("Stones", "Grains"): 98000,  # 1 stone = 98,000 grains
    ("Grains", "Stones"): 1 / 98000,  # 1 grain = 0.0000102 stones

    # Stones to Short Tons (US)
    ("Stones", "Short Tons (US)"): 0.007,  # 1 stone = 0.007 short tons
    ("Short Tons (US)", "Stones"): 1 / 0.007,  # 1 short ton = 142.857 stones

    # Stones to Long Tons (UK)
    ("Stones", "Long Tons (UK)"): 0.00625,  # 1 stone = 0.00625 long tons
    ("Long Tons (UK)", "Stones"): 1 / 0.00625,
    ("Carats", "Grains"): 3.08647,  # 1 carat = 3.08647 grains
    ("Grains", "Carats"): 1 / 3.08647,  # 1 grain = 0.324 carats
    ("Carats", "Long Tons (UK)"): 2.20462e-7,  # 1 carat = 2.20462e-7 long tons
    ("Long Tons (UK)", "Carats"): 1 / 2.20462e-7,  # 1 long ton = 4,535,924.9 carats

    # Carats to Short Tons (US)
    ("Carats", "Short Tons (US)"): 2.20462e-7,  # 1 carat = 2.20462e-7 short tons
    ("Short Tons (US)", "Carats"): 1 / 2.20462e-7,
    ("Grains", "Long Tons (UK)"): 6.4e-8,  # 1 grain = 6.4e-8 long tons
    ("Long Tons (UK)", "Grains"): 1 / 6.4e-8,  # 1 long ton = 15,680,000 grains

    # Grains to Short Tons (US)
    ("Grains", "Short Tons (US)"): 7.143e-8,  # 1 grain = 7.143e-8 short tons
    ("Short Tons (US)", "Grains"): 1 / 7.143e-8, 
    ("Long Tons (UK)", "Short Tons (US)"): 1.12,  # 1 Long Ton (UK) = 1.12 Short Tons (US)
    ("Short Tons (US)", "Long Tons (UK)"): 1 / 1.12,  
        ("Liters", "Milliliters"): 1000,
    ("Milliliters", "Liters"): 0.001,
    ("Liters", "Cubic Meters"): 0.001,
    ("Cubic Meters", "Liters"): 1000,
    ("Cubic Centimeters", "Liters"): 0.001,
    ("Liters", "Cubic Centimeters"): 1000,
    ("Cubic Millimeters", "Liters"): 1e-6,
    ("Liters", "Cubic Millimeters"): 1e6,

    # US & UK Gallons
    ("Liters", "Gallons (US)"): 0.264172,
    ("Gallons (US)", "Liters"): 3.78541,
    ("Liters", "Gallons (UK)"): 0.219969,
    ("Gallons (UK)", "Liters"): 4.54609,

    # Quarts
    ("Liters", "Quarts (US)"): 1.05669,
    ("Quarts (US)", "Liters"): 0.946353,
    ("Liters", "Quarts (UK)"): 0.879877,
    ("Quarts (UK)", "Liters"): 1.13652,

    # Pints
    ("Liters", "Pints (US)"): 2.11338,
    ("Pints (US)", "Liters"): 0.473176,
    ("Liters", "Pints (UK)"): 1.75975,
    ("Pints (UK)", "Liters"): 0.568261,

    # Fluid Ounces
    ("Liters", "Fluid Ounces (US)"): 33.814,
    ("Fluid Ounces (US)", "Liters"): 0.0295735,
    ("Liters", "Fluid Ounces (UK)"): 35.1951,
    ("Fluid Ounces (UK)", "Liters"): 0.0284131,

    # Cups
    ("Liters", "Cups (US)"): 4.22675,
    ("Cups (US)", "Liters"): 0.236588,
    ("Liters", "Cups (UK)"): 3.51951,
    ("Cups (UK)", "Liters"): 0.284131,

    # Tablespoons
    ("Liters", "Tablespoons (US)"): 67.628,
    ("Tablespoons (US)", "Liters"): 0.0147868,
    ("Liters", "Tablespoons (UK)"): 56.3121,
    ("Tablespoons (UK)", "Liters"): 0.0177582,

    # Teaspoons
    ("Liters", "Teaspoons (US)"): 202.884,
    ("Teaspoons (US)", "Liters"): 0.00492892,
    ("Liters", "Teaspoons (UK)"): 168.936,
    ("Teaspoons (UK)", "Liters"): 0.00591939,

    # Cubic Inches, Feet, and Yards
    ("Liters", "Cubic Inches"): 61.0237,
    ("Cubic Inches", "Liters"): 0.0163871,
    ("Liters", "Cubic Feet"): 0.0353147,
    ("Cubic Feet", "Liters"): 28.3168,
    ("Liters", "Cubic Yards"): 0.00130795,
    ("Cubic Yards", "Liters"): 764.555,
    ("Milliliters", "Cubic Meters"): 1e-6,
    ("Cubic Meters", "Milliliters"): 1e6,
    ("Milliliters", "Cubic Centimeters"): 1,  # 1 mL = 1 cm³
    ("Cubic Centimeters", "Milliliters"): 1,

    ("Milliliters", "Cubic Millimeters"): 1000,  # 1 mL = 1000 mm³
    ("Cubic Millimeters", "Milliliters"): 1 / 1000,

    ("Milliliters", "Cubic Inches"): 0.0610237,  # 1 mL = 0.0610237 in³
    ("Cubic Inches", "Milliliters"): 1 / 0.0610237,

    ("Milliliters", "Cubic Feet"): 3.5315e-5,  # 1 mL = 3.5315 × 10⁻⁵ ft³
    ("Cubic Feet", "Milliliters"): 1 / 3.5315e-5,

    ("Milliliters", "Cubic Yards"): 1.30795e-6,  # 1 mL = 1.30795 × 10⁻⁶ yd³
    ("Cubic Yards", "Milliliters"): 1 / 1.30795e-6,

    ("Milliliters", "Gallons (US)"): 0.000264172,  # 1 mL = 0.000264172 gal (US)
    ("Gallons (US)", "Milliliters"): 1 / 0.000264172,

    ("Milliliters", "Gallons (UK)"): 0.000219969,  # 1 mL = 0.000219969 gal (UK)
    ("Gallons (UK)", "Milliliters"): 1 / 0.000219969,

    ("Milliliters", "Quarts (US)"): 0.00105669,  # 1 mL = 0.00105669 qt (US)
    ("Quarts (US)", "Milliliters"): 1 / 0.00105669,

    ("Milliliters", "Pints (US)"): 0.00211338,  # 1 mL = 0.00211338 pt (US)
    ("Pints (US)", "Milliliters"): 1 / 0.00211338,

    ("Milliliters", "Pints (UK)"): 0.00175975,  # 1 mL = 0.00175975 pt (UK)
    ("Pints (UK)", "Milliliters"): 1 / 0.00175975,

    ("Milliliters", "Fluid Ounces (US)"): 0.033814,  # 1 mL = 0.033814 fl oz (US)
    ("Fluid Ounces (US)", "Milliliters"): 1 / 0.033814,

    ("Milliliters", "Fluid Ounces (UK)"): 0.0351951,  # 1 mL = 0.0351951 fl oz (UK)
    ("Fluid Ounces (UK)", "Milliliters"): 1 / 0.0351951,

    ("Milliliters", "Cups (US)"): 0.00422675,  # 1 mL = 0.00422675 cup (US)
    ("Cups (US)", "Milliliters"): 1 / 0.00422675,

    ("Milliliters", "Cups (UK)"): 0.00351951,  # 1 mL = 0.00351951 cup (UK)
    ("Cups (UK)", "Milliliters"): 1 / 0.00351951,

    ("Milliliters", "Tablespoons (US)"): 0.067628,  # 1 mL = 0.067628 tbsp (US)
    ("Tablespoons (US)", "Milliliters"): 1 / 0.067628,

    ("Milliliters", "Tablespoons (UK)"): 0.0563121,  # 1 mL = 0.0563121 tbsp (UK)
    ("Tablespoons (UK)", "Milliliters"): 1 / 0.0563121,

    ("Milliliters", "Teaspoons (US)"): 0.202884,  # 1 mL = 0.202884 tsp (US)
    ("Teaspoons (US)", "Milliliters"): 1 / 0.202884,

    ("Milliliters", "Teaspoons (UK)"): 0.168936,  # 1 mL = 0.168936 tsp (UK)
    ("Teaspoons (UK)", "Milliliters"): 1 / 0.168936,
            # Cubic Meters to other volume units
    ("Cubic Meters", "Cubic Centimeters"): 1e6,  # 1 m³ = 1,000,000 cm³
    ("Cubic Meters", "Cubic Millimeters"): 1e9,  # 1 m³ = 1,000,000,000 mm³
    ("Cubic Meters", "Cubic Inches"): 61023.7441,  # 1 m³ = 61,023.7441 in³
    ("Cubic Meters", "Cubic Feet"): 35.3147,  # 1 m³ = 35.3147 ft³
    ("Cubic Meters", "Cubic Yards"): 1.30795,  # 1 m³ = 1.30795 yd³
    ("Cubic Meters", "Gallons (US)"): 264.172,  # 1 m³ = 264.172 gal (US)
    ("Cubic Meters", "Gallons (UK)"): 219.969,  # 1 m³ = 219.969 gal (UK)
    ("Cubic Meters", "Quarts (US)"): 1056.69,  # 1 m³ = 1,056.69 qt (US)
    ("Cubic Meters", "Pints (US)"): 2113.38,  # 1 m³ = 2,113.38 pt (US)
    ("Cubic Meters", "Pints (UK)"): 1759.75,  # 1 m³ = 1,759.75 pt (UK)
    ("Cubic Meters", "Fluid Ounces (US)"): 33814,  # 1 m³ = 33,814 fl oz (US)
    ("Cubic Meters", "Fluid Ounces (UK)"): 35195.1,  # 1 m³ = 35,195.1 fl oz (UK)
    ("Cubic Meters", "Cups (US)"): 4226.75,  # 1 m³ = 4,226.75 cups (US)
    ("Cubic Meters", "Cups (UK)"): 3519.51,  # 1 m³ = 3,519.51 cups (UK)
    ("Cubic Meters", "Tablespoons (US)"): 67628,  # 1 m³ = 67,628 tbsp (US)
    ("Cubic Meters", "Tablespoons (UK)"): 56312,  # 1 m³ = 56,312 tbsp (UK)
    ("Cubic Meters", "Teaspoons (US)"): 202884,  # 1 m³ = 202,884 tsp (US)
    ("Cubic Meters", "Teaspoons (UK)"): 168936,  # 1 m³ = 168,936 tsp (UK)
    # Cubic Centimeters to other volume units
    ("Cubic Centimeters", "Cubic Millimeters"): 1000,  # 1 cm³ = 1000 mm³
    ("Cubic Centimeters", "Cubic Inches"): 0.0610237,  # 1 cm³ = 0.0610237 in³
    ("Cubic Centimeters", "Cubic Feet"): 3.5315e-5,  # 1 cm³ = 3.5315 × 10⁻⁵ ft³
    ("Cubic Centimeters", "Cubic Yards"): 1.308e-6,  # 1 cm³ = 1.308 × 10⁻⁶ yd³
    ("Cubic Centimeters", "Gallons (US)"): 0.000264172,  # 1 cm³ = 0.000264172 gal (US)
    ("Cubic Centimeters", "Gallons (UK)"): 0.000219969,  # 1 cm³ = 0.000219969 gal (UK)
    ("Cubic Centimeters", "Quarts (US)"): 0.00105669,  # 1 cm³ = 0.00105669 qt (US)
    ("Cubic Centimeters", "Pints (US)"): 0.00211338,  # 1 cm³ = 0.00211338 pt (US)
    ("Cubic Centimeters", "Pints (UK)"): 0.00175975,  # 1 cm³ = 0.00175975 pt (UK)
    ("Cubic Centimeters", "Fluid Ounces (US)"): 0.033814,  # 1 cm³ = 0.033814 fl oz (US)
    ("Cubic Centimeters", "Fluid Ounces (UK)"): 0.0351951,  # 1 cm³ = 0.0351951 fl oz (UK)
    ("Cubic Centimeters", "Cups (US)"): 0.00422675,  # 1 cm³ = 0.00422675 cups (US)
    ("Cubic Centimeters", "Cups (UK)"): 0.00351951,  # 1 cm³ = 0.00351951 cups (UK)
    ("Cubic Centimeters", "Tablespoons (US)"): 0.067628,  # 1 cm³ = 0.067628 tbsp (US)
    ("Cubic Centimeters", "Tablespoons (UK)"): 0.056312,  # 1 cm³ = 0.056312 tbsp (UK)
    ("Cubic Centimeters", "Teaspoons (US)"): 0.202884,  # 1 cm³ = 0.202884 tsp (US)
    ("Cubic Centimeters", "Teaspoons (UK)"): 0.168936,  # 1 cm³ = 0.168936 tsp (UK)
    # Cubic Inches to other volume units
    ("Cubic Inches", "Cubic Millimeters"): 16387.064,  # 1 in³ = 16387.064 mm³
    ("Cubic Inches", "Cubic Centimeters"): 16.3871,  # 1 in³ = 16.3871 cm³
    ("Cubic Inches", "Cubic Feet"): 0.000578704,  # 1 in³ = 0.000578704 ft³
    ("Cubic Inches", "Cubic Yards"): 2.1433e-5,  # 1 in³ = 2.1433 × 10⁻⁵ yd³
    ("Cubic Inches", "Gallons (US)"): 0.004329,  # 1 in³ = 0.004329 gal (US)
    ("Cubic Inches", "Gallons (UK)"): 0.003604,  # 1 in³ = 0.003604 gal (UK)
    ("Cubic Inches", "Quarts (US)"): 0.017316,  # 1 in³ = 0.017316 qt (US)
    ("Cubic Inches", "Pints (US)"): 0.034632,  # 1 in³ = 0.034632 pt (US)
    ("Cubic Inches", "Pints (UK)"): 0.02883,  # 1 in³ = 0.02883 pt (UK)
    ("Cubic Inches", "Fluid Ounces (US)"): 0.554113,  # 1 in³ = 0.554113 fl oz (US)
    ("Cubic Inches", "Fluid Ounces (UK)"): 0.576744,  # 1 in³ = 0.576744 fl oz (UK)
    ("Cubic Inches", "Cups (US)"): 0.069264,  # 1 in³ = 0.069264 cups (US)
    ("Cubic Inches", "Cups (UK)"): 0.05766,  # 1 in³ = 0.05766 cups (UK)
    ("Cubic Inches", "Tablespoons (US)"): 1.1082,  # 1 in³ = 1.1082 tbsp (US)
    ("Cubic Inches", "Tablespoons (UK)"): 0.92279,  # 1 in³ = 0.92279 tbsp (UK)
    ("Cubic Inches", "Teaspoons (US)"): 3.3246,  # 1 in³ = 3.3246 tsp (US)
    ("Cubic Inches", "Teaspoons (UK)"): 2.7684,  # 1 in³ = 2.7684 tsp (UK)
    # Cubic Feet to other volume units
    ("Cubic Feet", "Cubic Millimeters"): 28316846.6,  # 1 ft³ = 28,316,846.6 mm³
    ("Cubic Feet", "Cubic Centimeters"): 28316.8466,  # 1 ft³ = 28,316.8466 cm³
    ("Cubic Feet", "Cubic Inches"): 1728,  # 1 ft³ = 1,728 in³
    ("Cubic Feet", "Cubic Yards"): 0.037037,  # 1 ft³ = 0.037037 yd³
    ("Cubic Feet", "Gallons (US)"): 7.48052,  # 1 ft³ = 7.48052 gal (US)
    ("Cubic Feet", "Gallons (UK)"): 6.22884,  # 1 ft³ = 6.22884 gal (UK)
    ("Cubic Feet", "Quarts (US)"): 29.9221,  # 1 ft³ = 29.9221 qt (US)
    ("Cubic Feet", "Pints (US)"): 59.8442,  # 1 ft³ = 59.8442 pt (US)
    ("Cubic Feet", "Pints (UK)"): 49.8307,  # 1 ft³ = 49.8307 pt (UK)
    ("Cubic Feet", "Fluid Ounces (US)"): 957.506,  # 1 ft³ = 957.506 fl oz (US)
    ("Cubic Feet", "Fluid Ounces (UK)"): 996.614,  # 1 ft³ = 996.614 fl oz (UK)
    ("Cubic Feet", "Cups (US)"): 119.688,  # 1 ft³ = 119.688 cups (US)
    ("Cubic Feet", "Cups (UK)"): 99.6614,  # 1 ft³ = 99.6614 cups (UK)
    ("Cubic Feet", "Tablespoons (US)"): 1915.01,  # 1 ft³ = 1,915.01 tbsp (US)
    ("Cubic Feet", "Tablespoons (UK)"): 1594.58,  # 1 ft³ = 1,594.58 tbsp (UK)
    ("Cubic Feet", "Teaspoons (US)"): 5745.03,  # 1 ft³ = 5,745.03 tsp (US)
    ("Cubic Feet", "Teaspoons (UK)"): 4783.74,  # 1 ft³ = 4,783.74 tsp (UK)
    # Cubic Yards to other volume units
    ("Cubic Yards", "Cubic Millimeters"): 764554857.98,  # 1 yd³ = 764,554,857.98 mm³
    ("Cubic Yards", "Cubic Centimeters"): 764554.85798,  # 1 yd³ = 764,554.85798 cm³
    ("Cubic Yards", "Cubic Inches"): 46656,  # 1 yd³ = 46,656 in³
    ("Cubic Yards", "Cubic Feet"): 27,  # 1 yd³ = 27 ft³
    ("Cubic Yards", "Gallons (US)"): 201.974,  # 1 yd³ = 201.974 gal (US)
    ("Cubic Yards", "Gallons (UK)"): 168.178,  # 1 yd³ = 168.178 gal (UK)
    ("Cubic Yards", "Quarts (US)"): 807.897,  # 1 yd³ = 807.897 qt (US)
    ("Cubic Yards", "Pints (US)"): 1615.79,  # 1 yd³ = 1,615.79 pt (US)
    ("Cubic Yards", "Pints (UK)"): 1345.42,  # 1 yd³ = 1,345.42 pt (UK)
    ("Cubic Yards", "Fluid Ounces (US)"): 25852.6,  # 1 yd³ = 25,852.6 fl oz (US)
    ("Cubic Yards", "Fluid Ounces (UK)"): 26908.4,  # 1 yd³ = 26,908.4 fl oz (UK)
    ("Cubic Yards", "Cups (US)"): 3231.58,  # 1 yd³ = 3,231.58 cups (US)
    ("Cubic Yards", "Cups (UK)"): 2690.84,  # 1 yd³ = 2,690.84 cups (UK)
    ("Cubic Yards", "Tablespoons (US)"): 51705.3,  # 1 yd³ = 51,705.3 tbsp (US)
    ("Cubic Yards", "Tablespoons (UK)"): 43053.5,  # 1 yd³ = 43,053.5 tbsp (UK)
    ("Cubic Yards", "Teaspoons (US)"): 155116,  # 1 yd³ = 155,116 tsp (US)
    ("Cubic Yards", "Teaspoons (UK)"): 129160,  # 1 yd³ = 129,160 tsp (UK)
    ("Cubic Feet", "Quarts (UK)"): 24.9154,  # 1 ft³ = 24.9154 qt (UK)
    ("Quarts (UK)", "Cubic Feet"): 1 / 24.9154,  # 1 qt (UK) = 0.04016 ft³
("Cubic Yards", "Quarts (UK)"): 748.052,  # 1 yd³ = 748.052 qt (UK)
    ("Quarts (UK)", "Cubic Yards"): 1 / 748.052,  # 1 qt (UK) = 0.001337 yd³
        ("Gallons (US)", "Cubic Millimeters"): 3785411.784,  # 1 gal (US) = 3,785,411.784 mm³
    ("Gallons (US)", "Gallons (UK)"): 0.832674,  # 1 gal (US) = 0.832674 gal (UK)
    ("Gallons (US)", "Quarts (US)"): 4,  # 1 gal (US) = 4 qt (US)
    ("Gallons (US)", "Quarts (UK)"): 3.3307,  # 1 gal (US) = 3.3307 qt (UK)
    ("Gallons (US)", "Pints (US)"): 8,  # 1 gal (US) = 8 pt (US)
    ("Gallons (US)", "Pints (UK)"): 6.66139,  # 1 gal (US) = 6.66139 pt (UK)
    ("Gallons (US)", "Fluid Ounces (US)"): 128,  # 1 gal (US) = 128 fl oz (US)
    ("Gallons (US)", "Fluid Ounces (UK)"): 133.228,  # 1 gal (US) = 133.228 fl oz (UK)
    ("Gallons (US)", "Cups (US)"): 16,  # 1 gal (US) = 16 cups (US)
    ("Gallons (US)", "Cups (UK)"): 13.3228,  # 1 gal (US) = 13.3228 cups (UK)
    ("Gallons (US)", "Tablespoons (US)"): 256,  # 1 gal (US) = 256 tbsp (US)
    ("Gallons (US)", "Tablespoons (UK)"): 213.165,  # 1 gal (US) = 213.165 tbsp (UK)
    ("Gallons (US)", "Teaspoons (US)"): 768,  # 1 gal (US) = 768 tsp (US)
    ("Gallons (US)", "Teaspoons (UK)"): 639.495,  # 1 gal (US) = 639.495 tsp (UK)

    # Reverse conversions
    ("Cubic Millimeters", "Gallons (US)"): 1 / 3785411.784,
    ("Gallons (UK)", "Gallons (US)"): 1 / 0.832674,
    ("Quarts (US)", "Gallons (US)"): 1 / 4,
    ("Quarts (UK)", "Gallons (US)"): 1 / 3.3307,
    ("Pints (US)", "Gallons (US)"): 1 / 8,
    ("Pints (UK)", "Gallons (US)"): 1 / 6.66139,
    ("Fluid Ounces (US)", "Gallons (US)"): 1 / 128,
    ("Fluid Ounces (UK)", "Gallons (US)"): 1 / 133.228,
    ("Cups (US)", "Gallons (US)"): 1 / 16,
    ("Cups (UK)", "Gallons (US)"): 1 / 13.3228,
    ("Tablespoons (US)", "Gallons (US)"): 1 / 256,
    ("Tablespoons (UK)", "Gallons (US)"): 1 / 213.165,
    ("Teaspoons (US)", "Gallons (US)"): 1 / 768,
    ("Teaspoons (UK)", "Gallons (US)"): 1 / 639.495,
    ("Gallons (UK)", "Cubic Millimeters"): 4546090,  # 1 gal (UK) = 4,546,090 mm³
    ("Gallons (UK)", "Quarts (US)"): 4.8038,  # 1 gal (UK) = 4.8038 qt (US)
    ("Gallons (UK)", "Quarts (UK)"): 4,  # 1 gal (UK) = 4 qt (UK)
    ("Gallons (UK)", "Pints (US)"): 9.6076,  # 1 gal (UK) = 9.6076 pt (US)
    ("Gallons (UK)", "Pints (UK)"): 8,  # 1 gal (UK) = 8 pt (UK)
    ("Gallons (UK)", "Fluid Ounces (US)"): 153.722,  # 1 gal (UK) = 153.722 fl oz (US)
    ("Gallons (UK)", "Fluid Ounces (UK)"): 160,  # 1 gal (UK) = 160 fl oz (UK)
    ("Gallons (UK)", "Cups (US)"): 19.2152,  # 1 gal (UK) = 19.2152 cups (US)
    ("Gallons (UK)", "Cups (UK)"): 16,  # 1 gal (UK) = 16 cups (UK)
    ("Gallons (UK)", "Tablespoons (US)"): 307.444,  # 1 gal (UK) = 307.444 tbsp (US)
    ("Gallons (UK)", "Tablespoons (UK)"): 256,  # 1 gal (UK) = 256 tbsp (UK)
    ("Gallons (UK)", "Teaspoons (US)"): 922.332,  # 1 gal (UK) = 922.332 tsp (US)
    ("Gallons (UK)", "Teaspoons (UK)"): 768,  # 1 gal (UK) = 768 tsp (UK)

    # Reverse conversions
    ("Cubic Millimeters", "Gallons (UK)"): 1 / 4546090,
    ("Quarts (US)", "Gallons (UK)"): 1 / 4.8038,
    ("Quarts (UK)", "Gallons (UK)"): 1 / 4,
    ("Pints (US)", "Gallons (UK)"): 1 / 9.6076,
    ("Pints (UK)", "Gallons (UK)"): 1 / 8,
    ("Fluid Ounces (US)", "Gallons (UK)"): 1 / 153.722,
    ("Fluid Ounces (UK)", "Gallons (UK)"): 1 / 160,
    ("Cups (US)", "Gallons (UK)"): 1 / 19.2152,
    ("Cups (UK)", "Gallons (UK)"): 1 / 16,
    ("Tablespoons (US)", "Gallons (UK)"): 1 / 307.444,
    ("Tablespoons (UK)", "Gallons (UK)"): 1 / 256,
    ("Teaspoons (US)", "Gallons (UK)"): 1 / 922.332,
    ("Teaspoons (UK)", "Gallons (UK)"): 1 / 768,
    ("Quarts (US)", "Cubic Millimeters"): 946352.946,  # 1 qt (US) = 946,352.946 mm³
    ("Cubic Millimeters", "Quarts (US)"): 1 / 946352.946,  # Reverse conversion
    ("Quarts (US)", "Quarts (UK)"): 0.832674,  # 1 qt (US) = 0.832674 qt (UK)
    ("Quarts (UK)", "Quarts (US)"): 1 / 0.832674,  # Reverse conversion

    ("Quarts (US)", "Pints (US)"): 2,  # 1 qt (US) = 2 pt (US)
    ("Pints (US)", "Quarts (US)"): 1 / 2,

    ("Quarts (US)", "Pints (UK)"): 1.66535,  # 1 qt (US) = 1.66535 pt (UK)
    ("Pints (UK)", "Quarts (US)"): 1 / 1.66535,

    ("Quarts (US)", "Fluid Ounces (US)"): 32,  # 1 qt (US) = 32 fl oz (US)
    ("Fluid Ounces (US)", "Quarts (US)"): 1 / 32,

    ("Quarts (US)", "Fluid Ounces (UK)"): 33.307,  # 1 qt (US) = 33.307 fl oz (UK)
    ("Fluid Ounces (UK)", "Quarts (US)"): 1 / 33.307,

    ("Quarts (US)", "Cups (US)"): 4,  # 1 qt (US) = 4 cups (US)
    ("Cups (US)", "Quarts (US)"): 1 / 4,

    ("Quarts (US)", "Cups (UK)"): 3.3307,  # 1 qt (US) = 3.3307 cups (UK)
    ("Cups (UK)", "Quarts (US)"): 1 / 3.3307,

    ("Quarts (US)", "Tablespoons (US)"): 64,  # 1 qt (US) = 64 tbsp (US)
    ("Tablespoons (US)", "Quarts (US)"): 1 / 64,

    ("Quarts (US)", "Tablespoons (UK)"): 53.291,  # 1 qt (US) = 53.291 tbsp (UK)
    ("Tablespoons (UK)", "Quarts (US)"): 1 / 53.291,

    ("Quarts (US)", "Teaspoons (US)"): 192,  # 1 qt (US) = 192 tsp (US)
    ("Teaspoons (US)", "Quarts (US)"): 1 / 192,

    ("Quarts (US)", "Teaspoons (UK)"): 159.874,  # 1 qt (US) = 159.874 tsp (UK)
    ("Teaspoons (UK)", "Quarts (US)"): 1 / 159.874,
    ("Quarts (UK)", "Milliliters"): 1136.52,  # 1 qt (UK) = 1136.52 mL
    ("Milliliters", "Quarts (UK)"): 1 / 1136.52,

    ("Quarts (UK)", "Cubic Meters"): 0.00113652,  # 1 qt (UK) = 0.00113652 m³
    ("Cubic Meters", "Quarts (UK)"): 1 / 0.00113652,

    ("Quarts (UK)", "Cubic Centimeters"): 1136.52,  # 1 qt (UK) = 1136.52 cm³
    ("Cubic Centimeters", "Quarts (UK)"): 1 / 1136.52,

    ("Quarts (UK)", "Cubic Millimeters"): 1.13652e+6,  # 1 qt (UK) = 1,136,520 mm³
    ("Cubic Millimeters", "Quarts (UK)"): 1 / 1.13652e+6,

    ("Quarts (UK)", "Cubic Inches"): 69.3549,  # 1 qt (UK) = 69.3549 in³
    ("Cubic Inches", "Quarts (UK)"): 1 / 69.3549,

    ("Quarts (UK)", "Pints (US)"): 2.4019,  # 1 qt (UK) = 2.4019 pt (US)
    ("Pints (US)", "Quarts (UK)"): 1 / 2.4019,

    ("Quarts (UK)", "Pints (UK)"): 2,  # 1 qt (UK) = 2 pt (UK)
    ("Pints (UK)", "Quarts (UK)"): 1 / 2,

    ("Quarts (UK)", "Fluid Ounces (US)"): 38.4304,  # 1 qt (UK) = 38.4304 fl oz (US)
    ("Fluid Ounces (US)", "Quarts (UK)"): 1 / 38.4304,

    ("Quarts (UK)", "Fluid Ounces (UK)"): 40,  # 1 qt (UK) = 40 fl oz (UK)
    ("Fluid Ounces (UK)", "Quarts (UK)"): 1 / 40,

    ("Quarts (UK)", "Cups (US)"): 4.8038,  # 1 qt (UK) = 4.8038 cups (US)
    ("Cups (US)", "Quarts (UK)"): 1 / 4.8038,

    ("Quarts (UK)", "Cups (UK)"): 4,  # 1 qt (UK) = 4 cups (UK)
    ("Cups (UK)", "Quarts (UK)"): 1 / 4,

    ("Quarts (UK)", "Tablespoons (US)"): 76.8608,  # 1 qt (UK) = 76.8608 tbsp (US)
    ("Tablespoons (US)", "Quarts (UK)"): 1 / 76.8608,

    ("Quarts (UK)", "Tablespoons (UK)"): 64,  # 1 qt (UK) = 64 tbsp (UK)
    ("Tablespoons (UK)", "Quarts (UK)"): 1 / 64,

    ("Quarts (UK)", "Teaspoons (US)"): 230.582,  # 1 qt (UK) = 230.582 tsp (US)
    ("Teaspoons (US)", "Quarts (UK)"): 1 / 230.582,

    ("Quarts (UK)", "Teaspoons (UK)"): 192,  # 1 qt (UK) = 192 tsp (UK)
    ("Teaspoons (UK)", "Quarts (UK)"): 1 / 192,
    ("Pints (US)", "Cubic Millimeters"): 473176,  # 1 pt (US) = 473,176 mm³
    ("Cubic Millimeters", "Pints (US)"): 1 / 473176,

    ("Pints (US)", "Pints (UK)"): 0.832674,  # 1 pt (US) = 0.832674 pt (UK)
    ("Pints (UK)", "Pints (US)"): 1 / 0.832674,

    ("Pints (US)", "Fluid Ounces (US)"): 16,  # 1 pt (US) = 16 fl oz (US)
    ("Fluid Ounces (US)", "Pints (US)"): 1 / 16,

    ("Pints (US)", "Fluid Ounces (UK)"): 16.6535,  # 1 pt (US) = 16.6535 fl oz (UK)
    ("Fluid Ounces (UK)", "Pints (US)"): 1 / 16.6535,

    ("Pints (US)", "Cups (US)"): 2,  # 1 pt (US) = 2 cups (US)
    ("Cups (US)", "Pints (US)"): 1 / 2,

    ("Pints (US)", "Cups (UK)"): 1.66535,  # 1 pt (US) = 1.66535 cups (UK)
    ("Cups (UK)", "Pints (US)"): 1 / 1.66535,

    ("Pints (US)", "Tablespoons (US)"): 32,  # 1 pt (US) = 32 tbsp (US)
    ("Tablespoons (US)", "Pints (US)"): 1 / 32,

    ("Pints (US)", "Teaspoons (UK)"): 96,  # 1 pt (US) = 96 tsp (UK)
    ("Teaspoons (UK)", "Pints (US)"): 1 / 96,
    ("Pints (UK)", "Cubic Millimeters"): 568261,  # 1 pt (UK) = 568,261 mm³
    ("Cubic Millimeters", "Pints (UK)"): 1 / 568261,

    ("Pints (UK)", "Fluid Ounces (US)"): 19.2152,  # 1 pt (UK) = 19.2152 fl oz (US)
    ("Fluid Ounces (US)", "Pints (UK)"): 1 / 19.2152,

    ("Pints (UK)", "Fluid Ounces (UK)"): 20,  # 1 pt (UK) = 20 fl oz (UK)
    ("Fluid Ounces (UK)", "Pints (UK)"): 1 / 20,

    ("Pints (UK)", "Cups (US)"): 2.4019,  # 1 pt (UK) = 2.4019 cups (US)
    ("Cups (US)", "Pints (UK)"): 1 / 2.4019,

    ("Pints (UK)", "Cups (UK)"): 2,  # 1 pt (UK) = 2 cups (UK)
    ("Cups (UK)", "Pints (UK)"): 1 / 2,

    ("Pints (UK)", "Tablespoons (US)"): 38.4304,  # 1 pt (UK) = 38.4304 tbsp (US)
    ("Tablespoons (US)", "Pints (UK)"): 1 / 38.4304,

    ("Pints (UK)", "Teaspoons (UK)"): 120,  # 1 pt (UK) = 120 tsp (UK)
    ("Teaspoons (UK)", "Pints (UK)"): 1 / 120,
    ("Pints (UK)", "Tablespoons (UK)"): 32,  # 1 pt (UK) = 32 tbsp (UK)
    ("Tablespoons (UK)", "Pints (UK)"): 1 / 32,
    ("Fluid Ounces (US)", "Cubic Millimeters"): 29573.5,  # 1 fl oz (US) = 29,573.5 mm³
    ("Fluid Ounces (US)", "Fluid Ounces (UK)"): 0.96076,  # 1 fl oz (US) = 0.96076 fl oz (UK)
    ("Fluid Ounces (US)", "Cups (US)"): 0.125,  # 1 fl oz (US) = 0.125 cups (US)
    ("Fluid Ounces (US)", "Cups (UK)"): 0.104,  # 1 fl oz (US) = 0.104 cups (UK)
    ("Fluid Ounces (US)", "Tablespoons (US)"): 2,  # 1 fl oz (US) = 2 tbsp (US)
    ("Fluid Ounces (US)", "Tablespoons (UK)"): 1.6,  # 1 fl oz (US) = 1.6 tbsp (UK)
    ("Fluid Ounces (US)", "Teaspoons (US)"): 6,  # 1 fl oz (US) = 6 tsp (US)
    ("Fluid Ounces (US)", "Teaspoons (UK)"): 4.8,  # 1 fl oz (US) = 4.8 tsp (UK)
    ("Cubic Millimeters", "Fluid Ounces (US)"): 1 / 29573.5,
    ("Fluid Ounces (UK)", "Fluid Ounces (US)"): 1 / 0.96076,
    ("Cups (US)", "Fluid Ounces (US)"): 1 / 0.125,
    ("Cups (UK)", "Fluid Ounces (US)"): 1 / 0.104,
    ("Tablespoons (US)", "Fluid Ounces (US)"): 1 / 2,
    ("Tablespoons (UK)", "Fluid Ounces (US)"): 1 / 1.6,
    ("Teaspoons (US)", "Fluid Ounces (US)"): 1 / 6,
    ("Teaspoons (UK)", "Fluid Ounces (US)"): 1 / 4.8,
    ("Fluid Ounces (UK)", "Cubic Millimeters"): 28413.1,  # 1 fl oz (UK) = 28,413.1 mm³
    ("Fluid Ounces (UK)", "Cups (US)"): 0.12,  # 1 fl oz (UK) = 0.12 cups (US)
    ("Fluid Ounces (UK)", "Cups (UK)"): 0.1,  # 1 fl oz (UK) = 0.1 cups (UK)
    ("Fluid Ounces (UK)", "Tablespoons (US)"): 1.92,  # 1 fl oz (UK) = 1.92 tbsp (US)
    ("Fluid Ounces (UK)", "Tablespoons (UK)"): 1.6,  # 1 fl oz (UK) = 1.6 tbsp (UK)
    ("Fluid Ounces (UK)", "Teaspoons (US)"): 5.76,  # 1 fl oz (UK) = 5.76 tsp (US)
    ("Fluid Ounces (UK)", "Teaspoons (UK)"): 4.8,  # 1 fl oz (UK) = 4.8 tsp (UK)
    ("Cubic Millimeters", "Fluid Ounces (UK)"): 1 / 28413.1,
    ("Cups (US)", "Fluid Ounces (UK)"): 1 / 0.12,
    ("Cups (UK)", "Fluid Ounces (UK)"): 1 / 0.1,
    ("Tablespoons (US)", "Fluid Ounces (UK)"): 1 / 1.92,
    ("Tablespoons (UK)", "Fluid Ounces (UK)"): 1 / 1.6,
    ("Teaspoons (US)", "Fluid Ounces (UK)"): 1 / 5.76,
    ("Teaspoons (UK)", "Fluid Ounces (UK)"): 1 / 4.8,
    ("Cups (US)", "Cubic Millimeters"): 236588.24,  # 1 cup (US) = 236,588.24 mm³
    ("Cups (US)", "Cups (UK)"): 0.83267,  # 1 cup (US) = 0.83267 cups (UK)
    ("Cups (US)", "Tablespoons (US)"): 16,  # 1 cup (US) = 16 tbsp (US)
    ("Cups (US)", "Tablespoons (UK)"): 13.33,  # 1 cup (US) = 13.33 tbsp (UK)
    ("Cups (US)", "Teaspoons (US)"): 48,  # 1 cup (US) = 48 tsp (US)
    ("Cups (US)", "Teaspoons (UK)"): 39.99,  # 1 cup (US) = 39.99 tsp (UK)
    ("Cubic Millimeters", "Cups (US)"): 1 / 236588.24,
    ("Cups (UK)", "Cups (US)"): 1 / 0.83267,
    ("Tablespoons (US)", "Cups (US)"): 1 / 16,
    ("Tablespoons (UK)", "Cups (US)"): 1 / 13.33,
    ("Teaspoons (US)", "Cups (US)"): 1 / 48,
    ("Teaspoons (UK)", "Cups (US)"): 1 / 39.99,
    ("Cups (UK)", "Cubic Millimeters"): 284130.62,  # 1 cup (UK) = 284,130.62 mm³
    ("Cups (UK)", "Tablespoons (US)"): 18.43,  # 1 cup (UK) = 18.43 tbsp (US)
    ("Cups (UK)", "Tablespoons (UK)"): 16,  # 1 cup (UK) = 16 tbsp (UK)
    ("Cups (UK)", "Teaspoons (US)"): 55.3,  # 1 cup (UK) = 55.3 tsp (US)
    ("Cups (UK)", "Teaspoons (UK)"): 48,  # 1 cup (UK) = 48 tsp (UK)
    ("Cubic Millimeters", "Cups (UK)"): 1 / 284130.62,
    ("Tablespoons (US)", "Cups (UK)"): 1 / 18.43,
    ("Tablespoons (UK)", "Cups (UK)"): 1 / 16,
    ("Teaspoons (US)", "Cups (UK)"): 1 / 55.3,
    ("Teaspoons (UK)", "Cups (UK)"): 1 / 48,
    ("Tablespoons (US)", "Cubic Millimeters"): 14786.764,  # 1 tbsp (US) = 14,786.764 mm³
    ("Tablespoons (US)", "Tablespoons (UK)"): 0.8327,  # 1 tbsp (US) = 0.8327 tbsp (UK)
    ("Tablespoons (US)", "Teaspoons (US)"): 3,  # 1 tbsp (US) = 3 tsp (US)
    ("Tablespoons (US)", "Teaspoons (UK)"): 2.5,  # 1 tbsp (US) = 2.5 tsp (UK)
    ("Cubic Millimeters", "Tablespoons (US)"): 1 / 14786.764,
    ("Tablespoons (UK)", "Tablespoons (US)"): 1 / 0.8327,
    ("Teaspoons (US)", "Tablespoons (US)"): 1 / 3,
    ("Teaspoons (UK)", "Tablespoons (US)"): 1 / 2.5,
    ("Tablespoons (UK)", "Cubic Millimeters"): 17071.429,  # 1 tbsp (UK) = 17,071.429 mm³
    ("Tablespoons (UK)", "Teaspoons (US)"): 3.6,  # 1 tbsp (UK) = 3.6 tsp (US)
    ("Tablespoons (UK)", "Teaspoons (UK)"): 3,  # 1 tbsp (UK) = 3 tsp (UK)
    ("Cubic Millimeters", "Tablespoons (UK)"): 1 / 17071.429,
    ("Teaspoons (US)", "Tablespoons (UK)"): 1 / 3.6,
    ("Teaspoons (UK)", "Tablespoons (UK)"): 1 / 3,
    ("Teaspoons (US)", "Cubic Millimeters"): 4928.92,  # 1 tsp (US) = 4,928.92 mm³
    ("Teaspoons (US)", "Teaspoons (UK)"): 0.83267,  # 1 tsp (US) = 0.83267 tsp (UK)
    ("Cubic Millimeters", "Teaspoons (US)"): 1 / 4928.92,
    ("Teaspoons (UK)", "Teaspoons (US)"): 1 / 0.83267,
    # Time conversions
    ("Seconds", "Minutes"): 1 / 60,
    ("Seconds", "Hours"): 1 / 3600,
    ("Seconds", "Days"): 1 / 86400,
    ("Seconds", "Weeks"): 1 / 604800,
    ("Seconds", "Months"): 1 / 2.628e+6,  # Approximate (30.44 days)
    ("Seconds", "Years"): 1 / 3.154e+7,   # Approximate (365.25 days)
    ("Seconds", "Decades"): 1 / 3.154e+8,  # Approximate (10 years)
    ("Seconds", "Centuries"): 1 / 3.154e+9, # Approximate (100 years)
    ("Seconds", "Millennia"): 1 / 3.154e+10, # Approximate (1000 years)

    ("Minutes", "Seconds"): 60,
    ("Minutes", "Hours"): 1 / 60,
    ("Minutes", "Days"): 1 / 1440,
    ("Minutes", "Weeks"): 1 / 10080,
    ("Minutes", "Months"): 1 / 43800,   # Approximate
    ("Minutes", "Years"): 1 / 525600,   # Approximate
    ("Minutes", "Decades"): 1 / 5.256e+6,
    ("Minutes", "Centuries"): 1 / 5.256e+7,
    ("Minutes", "Millennia"): 1 / 5.256e+8,

    ("Hours", "Seconds"): 3600,
    ("Hours", "Minutes"): 60,
    ("Hours", "Days"): 1 / 24,
    ("Hours", "Weeks"): 1 / 168,
    ("Hours", "Months"): 1 / 730,  # Approximate
    ("Hours", "Years"): 1 / 8760,  # Approximate
    ("Hours", "Decades"): 1 / 87600,
    ("Hours", "Centuries"): 1 / 876000,
    ("Hours", "Millennia"): 1 / 8.76e+6,

    ("Days", "Seconds"): 86400,
    ("Days", "Minutes"): 1440,
    ("Days", "Hours"): 24,
    ("Days", "Weeks"): 1 / 7,
    ("Days", "Months"): 1 / 30.44,  # Approximate
    ("Days", "Years"): 1 / 365.25,
    ("Days", "Decades"): 1 / 3652.5,
    ("Days", "Centuries"): 1 / 36525,
    ("Days", "Millennia"): 1 / 365250,

    ("Weeks", "Seconds"): 604800,
    ("Weeks", "Minutes"): 10080,
    ("Weeks", "Hours"): 168,
    ("Weeks", "Days"): 7,
    ("Weeks", "Months"): 1 / 4.348,  # Approximate
    ("Weeks", "Years"): 1 / 52.1775,
    ("Weeks", "Decades"): 1 / 521.775,
    ("Weeks", "Centuries"): 1 / 5217.75,
    ("Weeks", "Millennia"): 1 / 52177.5,

    ("Months", "Seconds"): 2.628e+6,
    ("Months", "Minutes"): 43800,
    ("Months", "Hours"): 730,
    ("Months", "Days"): 30.44,  # Approximate
    ("Months", "Weeks"): 4.348,  # Approximate
    ("Months", "Years"): 1 / 12,
    ("Months", "Decades"): 1 / 120,
    ("Months", "Centuries"): 1 / 1200,
    ("Months", "Millennia"): 1 / 12000,

    ("Years", "Seconds"): 3.154e+7,
    ("Years", "Minutes"): 525600,
    ("Years", "Hours"): 8760,
    ("Years", "Days"): 365.25,  # Leap year considered
    ("Years", "Weeks"): 52.1775,
    ("Years", "Months"): 12,
    ("Years", "Decades"): 1 / 10,
    ("Years", "Centuries"): 1 / 100,
    ("Years", "Millennia"): 1 / 1000,

    ("Decades", "Seconds"): 3.154e+8,
    ("Decades", "Minutes"): 5.256e+6,
    ("Decades", "Hours"): 87600,
    ("Decades", "Days"): 3652.5,  # Approximate
    ("Decades", "Weeks"): 521.775,
    ("Decades", "Months"): 120,
    ("Decades", "Years"): 10,
    ("Decades", "Centuries"): 1 / 10,
    ("Decades", "Millennia"): 1 / 100,

    ("Centuries", "Seconds"): 3.154e+9,
    ("Centuries", "Minutes"): 5.256e+7,
    ("Centuries", "Hours"): 876000,
    ("Centuries", "Days"): 36525,  # Approximate
    ("Centuries", "Weeks"): 5217.75,
    ("Centuries", "Months"): 1200,
    ("Centuries", "Years"): 100,
    ("Centuries", "Decades"): 10,
    ("Centuries", "Millennia"): 1 / 10,

    ("Millennia", "Seconds"): 3.154e+10,
    ("Millennia", "Minutes"): 5.256e+8,
    ("Millennia", "Hours"): 8.76e+6,
    ("Millennia", "Days"): 365250,  # Approximate
    ("Millennia", "Weeks"): 52177.5,
    ("Millennia", "Months"): 12000,
    ("Millennia", "Years"): 1000,
    ("Millennia", "Decades"): 100,
    ("Millennia", "Centuries"): 10,

    ("Seconds", "Minutes"): 1 / 60,
    ("Seconds", "Hours"): 1 / 3600,
    ("Seconds", "Days"): 1 / 86400,
    ("Seconds", "Weeks"): 1 / 604800,
    ("Seconds", "Months"): 1 / 2.628e+6,
    ("Seconds", "Years"): 1 / 3.154e+7,
    ("Seconds", "Decades"): 1 / 3.154e+8,
    ("Seconds", "Centuries"): 1 / 3.154e+9,
    ("Seconds", "Millennia"): 1 / 3.154e+10,
("Seconds", "Minutes"): 1 / 60,
    ("Seconds", "Hours"): 1 / 3600,
    ("Seconds", "Days"): 1 / 86400,
    ("Seconds", "Weeks"): 1 / 604800,
    ("Seconds", "Months"): 1 / 2628000,  # Approximate
    ("Seconds", "Years"): 1 / 31536000,  # Approximate
    ("Seconds", "Decades"): 1 / 315360000,
    ("Seconds", "Centuries"): 1 / 3153600000,
    ("Seconds", "Millennia"): 1 / 31536000000,

    ("Minutes", "Seconds"): 60,
    ("Minutes", "Hours"): 1 / 60,
    ("Minutes", "Days"): 1 / 1440,
    ("Minutes", "Weeks"): 1 / 10080,
    ("Minutes", "Months"): 1 / 43800,  # Approximate
    ("Minutes", "Years"): 1 / 525600,
    ("Minutes", "Decades"): 1 / 5256000,
    ("Minutes", "Centuries"): 1 / 52560000,
    ("Minutes", "Millennia"): 1 / 525600000,

    ("Hours", "Seconds"): 3600,
    ("Hours", "Minutes"): 60,
    ("Hours", "Days"): 1 / 24,
    ("Hours", "Weeks"): 1 / 168,
    ("Hours", "Months"): 1 / 730,  # Approximate
    ("Hours", "Years"): 1 / 8760,
    ("Hours", "Decades"): 1 / 87600,
    ("Hours", "Centuries"): 1 / 876000,
    ("Hours", "Millennia"): 1 / 8760000,

    ("Days", "Seconds"): 86400,
    ("Days", "Minutes"): 1440,
    ("Days", "Hours"): 24,
    ("Days", "Weeks"): 1 / 7,
    ("Days", "Months"): 1 / 30.44,  # Approximate
    ("Days", "Years"): 1 / 365.25,
    ("Days", "Decades"): 1 / 3652.5,
    ("Days", "Centuries"): 1 / 36525,
    ("Days", "Millennia"): 1 / 365250,

    ("Weeks", "Seconds"): 604800,
    ("Weeks", "Minutes"): 10080,
    ("Weeks", "Hours"): 168,
    ("Weeks", "Days"): 7,
    ("Weeks", "Months"): 1 / 4.345,  # Approximate
    ("Weeks", "Years"): 1 / 52.143,
    ("Weeks", "Decades"): 1 / 521.43,
    ("Weeks", "Centuries"): 1 / 5214.3,
    ("Weeks", "Millennia"): 1 / 52143,

    ("Months", "Seconds"): 2628000,  # Approximate
    ("Months", "Minutes"): 43800,
    ("Months", "Hours"): 730,
    ("Months", "Days"): 30.44,  # Approximate
    ("Months", "Weeks"): 4.345,  # Approximate
    ("Months", "Years"): 1 / 12,
    ("Months", "Decades"): 1 / 120,
    ("Months", "Centuries"): 1 / 1200,
    ("Months", "Millennia"): 1 / 12000,

    ("Years", "Seconds"): 31536000,  # Approximate
    ("Years", "Minutes"): 525600,
    ("Years", "Hours"): 8760,
    ("Years", "Days"): 365.25,
    ("Years", "Weeks"): 52.143,
    ("Years", "Months"): 12,
    ("Years", "Decades"): 1 / 10,
    ("Years", "Centuries"): 1 / 100,
    ("Years", "Millennia"): 1 / 1000,

    ("Decades", "Years"): 10,
    ("Decades", "Centuries"): 1 / 10,
    ("Decades", "Millennia"): 1 / 100,

    ("Centuries", "Years"): 100,
    ("Centuries", "Decades"): 10,
    ("Centuries", "Millennia"): 1 / 10,

    ("Millennia", "Years"): 1000,
    ("Millennia", "Decades"): 100,
    ("Millennia", "Centuries"): 10,
    # Speed conversions
    ("Meters per Second", "Kilometers per Hour"): 3.6,
    ("Meters per Second", "Miles per Hour"): 2.23694,
    ("Meters per Second", "Knots"): 1.94384,
    ("Meters per Second", "Feet per Second"): 3.28084,

    # Area conversions
    ("Square Meters", "Square Kilometers"): 1e-6,
    ("Square Meters", "Square Centimeters"): 10000,
    ("Square Meters", "Square Millimeters"): 1e6,
    ("Square Meters", "Square Inches"): 1550.0031,
    ("Square Meters", "Square Feet"): 10.7639,
    ("Square Meters", "Square Yards"): 1.19599,
    ("Square Meters", "Square Miles"): 3.861e-7,
    ("Square Meters", "Acres"): 0.000247105,
    ("Square Meters", "Hectares"): 0.0001,
    ("Kilometers per Hour", "Miles per Hour"): 0.621371,
    ("Miles per Hour", "Kilometers per Hour"): 1.60934,
    ("Kilometers per Hour", "Miles per Hour"): 0.621371,
    ("Miles per Hour", "Kilometers per Hour"): 1.60934,
    ("Kilometers per Hour", "Knots"): 0.539957,
    ("Knots", "Kilometers per Hour"): 1.852,
        ("Kilometers per Hour", "Miles per Hour"): 0.621371,
    ("Miles per Hour", "Kilometers per Hour"): 1.60934,
    ("Kilometers per Hour", "Knots"): 0.539957,
    ("Knots", "Kilometers per Hour"): 1.852,
    ("Kilometers per Hour", "Feet per Second"): 0.911344,
    ("Feet per Second", "Kilometers per Hour"): 1.09728,
    ("Miles per Hour", "Knots"): 0.868976,
    ("Knots", "Miles per Hour"): 1.15078,
    ("Miles per Hour", "Feet per Second"): 1.46667,  # ✅ Added this
    ("Feet per Second", "Miles per Hour"): 0.681818, # ✅ Added reverse conversion
     ("Knots", "Feet per Second"): 1.68781,
    ("Feet per Second", "Knots"): 0.592484,
    ("Square Kilometers", "Square Centimeters"): 10**10,
("Square Centimeters", "Square Kilometers"): 10**-10,
("Square Kilometers", "Square Inches"): 1.55e9,
("Square Kilometers", "Square Feet"): 1.076e7,
("Square Kilometers", "Square Yards"): 1.196e6,
("Square Kilometers", "Square Miles"): 0.3861,
("Square Kilometers", "Acres"): 247.105,
("Square Kilometers", "Hectares"): 100,

("Square Inches", "Square Kilometers"): 6.4516e-10,
("Square Feet", "Square Kilometers"): 9.2903e-8,
("Square Yards", "Square Kilometers"): 8.3613e-7,
("Square Miles", "Square Kilometers"): 2.58999,
("Acres", "Square Kilometers"): 0.004047,
("Hectares", "Square Kilometers"): 0.01,
("Square Centimeters", "Square Millimeters"): 100,
("Square Centimeters", "Square Inches"): 0.155,
("Square Centimeters", "Square Feet"): 0.001076,
("Square Centimeters", "Square Yards"): 0.0001196,
("Square Centimeters", "Square Miles"): 3.861e-11,
("Square Centimeters", "Acres"): 2.471e-8,
("Square Centimeters", "Hectares"): 1e-8,

("Square Millimeters", "Square Centimeters"): 0.01,
("Square Inches", "Square Centimeters"): 6.4516,
("Square Feet", "Square Centimeters"): 929.03,
("Square Yards", "Square Centimeters"): 8361.27,
("Square Miles", "Square Centimeters"): 2.59e+10,
("Acres", "Square Centimeters"): 40468564.224,
("Hectares", "Square Centimeters"): 100000000,
("Square Millimeters", "Square Kilometers"): 1e-12,
("Square Millimeters", "Square Inches"): 0.00155,
("Square Millimeters", "Square Feet"): 1.076e-5,
("Square Millimeters", "Square Yards"): 1.196e-6,
("Square Millimeters", "Square Miles"): 3.861e-13,
("Square Millimeters", "Acres"): 2.471e-10,
("Square Millimeters", "Hectares"): 1e-10,
("Square Kilometers", "Square Millimeters"): 1e+12,
("Square Inches", "Square Millimeters"): 645.16,
("Square Feet", "Square Millimeters"): 92903.04,
("Square Yards", "Square Millimeters"): 836127.36,
("Square Miles", "Square Millimeters"): 2.59e+15,
("Acres", "Square Millimeters"): 4046856422.4,
("Hectares", "Square Millimeters"): 1e+10,
("Square Inches", "Square Feet"): 0.00694444,
("Square Inches", "Square Yards"): 0.000771605,
("Square Inches", "Square Miles"): 2.491e-10,
("Square Inches", "Acres"): 1.5942e-7,
("Square Inches", "Hectares"): 6.4516e-8,

("Square Feet", "Square Inches"): 144,
("Square Yards", "Square Inches"): 1296,
("Square Miles", "Square Inches"): 4.014e+9,
("Acres", "Square Inches"): 6.273e+6,
("Hectares", "Square Inches"): 1.55e+7,
("Square Feet", "Square Yards"): 0.111111,
("Square Feet", "Square Miles"): 3.587e-8,
("Square Feet", "Acres"): 2.2957e-5,
("Square Feet", "Hectares"): 9.2903e-6,

("Square Yards", "Square Feet"): 9,
("Square Miles", "Square Feet"): 2.788e+7,
("Acres", "Square Feet"): 43560,
("Hectares", "Square Feet"): 107639,
("Square Yards", "Square Miles"): 3.2283e-7,
("Square Yards", "Acres"): 0.00020661,
("Square Yards", "Hectares"): 8.3613e-5,

("Square Miles", "Square Yards"): 3.098e+6,
("Acres", "Square Yards"): 4840,
("Hectares", "Square Yards"): 11959.9,
("Square Miles", "Acres"): 640,
("Square Miles", "Hectares"): 258.999,
("Acres", "Square Miles"): 1 / 640,
("Hectares", "Square Miles"): 1 / 258.999,
("Acres", "Hectares"): 0.404686,
("Hectares", "Acres"): 2.47105,

    ("Kilometers per Hour", "Miles per Hour"): 0.621371,
    ("Miles per Hour", "Kilometers per Hour"): 1.60934,
    ("Kilometers per Hour", "Knots"): 0.539957,
    ("Knots", "Kilometers per Hour"): 1.852,
    ("Kilometers per Hour", "Feet per Second"): 0.911344,
    ("Feet per Second", "Kilometers per Hour"): 1.09728,
    # Pressure conversions
    ("Pascals", "Kilopascals"): 1 / 1000,
    ("Pascals", "Megapascals"): 1 / 1e6,
    ("Pascals", "Bars"): 1 / 100000,
    ("Pascals", "Atmospheres"): 1 / 101325,
    ("Pascals", "Millimeters of Mercury"): 1 / 133.322,
    ("Pascals", "Inches of Mercury"): 1 / 3386.39,
# Pressure Conversions
("Kilopascals", "Megapascals"): 0.001,
("Kilopascals", "Bars"): 0.01,
("Kilopascals", "Atmospheres"): 0.00986923,
("Kilopascals", "Millimeters of Mercury"): 7.50062,
("Kilopascals", "Inches of Mercury"): 0.2953,

("Megapascals", "Kilopascals"): 1000,
("Bars", "Kilopascals"): 100,
("Atmospheres", "Kilopascals"): 101.325,
("Millimeters of Mercury", "Kilopascals"): 0.133322,
("Inches of Mercury", "Kilopascals"): 3.38639,
# Pressure Conversions
("Megapascals", "Bars"): 10,
("Megapascals", "Atmospheres"): 9.86923,
("Megapascals", "Millimeters of Mercury"): 7500.62,
("Megapascals", "Inches of Mercury"): 295.3,

("Bars", "Megapascals"): 0.1,
("Atmospheres", "Megapascals"): 0.101325,
("Millimeters of Mercury", "Megapascals"): 0.000133322,
("Inches of Mercury", "Megapascals"): 0.00338639,
# Pressure Conversions
("Bars", "Atmospheres"): 0.986923,
("Bars", "Millimeters of Mercury"): 750.062,
("Bars", "Inches of Mercury"): 29.53,

("Atmospheres", "Bars"): 1.01325,
("Millimeters of Mercury", "Bars"): 0.00133322,
("Inches of Mercury", "Bars"): 0.0338639,
# Pressure Conversions
("Atmospheres", "Millimeters of Mercury"): 760,
("Atmospheres", "Inches of Mercury"): 29.9213,

("Millimeters of Mercury", "Atmospheres"): 1 / 760,
("Inches of Mercury", "Atmospheres"): 1 / 29.9213,
# Pressure Conversions
("Millimeters of Mercury", "Inches of Mercury"): 1 / 25.4,
("Inches of Mercury", "Millimeters of Mercury"): 25.4,

    # Power conversions
    ("Watts", "Kilowatts"): 1 / 1000,
    ("Watts", "Megawatts"): 1 / 1e6,
    ("Watts", "Horsepower"): 1 / 745.7,
# Power Conversions
("Kilowatts", "Megawatts"): 1 / 1000,
("Megawatts", "Kilowatts"): 1000,
("Kilowatts", "Horsepower"): 1.34102,
("Horsepower", "Kilowatts"): 1 / 1.34102,
# Power Conversions
("Megawatts", "Horsepower"): 1341.02,  # 1 Megawatt = 1341.02 Horsepower
("Horsepower", "Megawatts"): 1 / 1341.02,

    # Energy conversions
    ("Joules", "Kilojoules"): 1 / 1000,
    ("Joules", "Calories"): 1 / 4.184,
    ("Joules", "Kilocalories"): 1 / 4184,
    ("Joules", "Electronvolts"): 6.242e+18,
    ("Joules", "BTU"): 1 / 1055.06,
# Energy Conversions
("Kilojoules", "Calories"): 239.006,  # 1 Kilojoule = 239.006 Calories
("Kilojoules", "Kilocalories"): 0.239006,  # 1 Kilojoule = 0.239006 Kilocalories
("Kilojoules", "BTU"): 0.947817,  # 1 Kilojoule = 0.947817 BTU

("Calories", "Kilojoules"): 1 / 239.006,
("Kilocalories", "Kilojoules"): 1 / 0.239006,
("BTU", "Kilojoules"): 1 / 0.947817,
# Energy Conversions
("Calories", "Kilocalories"): 0.001,  # 1 Calorie = 0.001 Kilocalories
("Calories", "Electronvolts"): 2.6132e19,  # 1 Calorie = 2.6132 × 10^19 Electronvolts
("Calories", "BTU"): 0.00396567,  # 1 Calorie = 0.00396567 BTU

("Kilocalories", "Calories"): 1000,  # 1 Kilocalorie = 1000 Calories
("Electronvolts", "Calories"): 1 / 2.6132e19,
("BTU", "Calories"): 1 / 0.00396567,
# Energy Conversions
("Kilocalories", "Electronvolts"): 2.6132e22,  # 1 Kilocalorie = 2.6132 × 10^22 Electronvolts
("Kilocalories", "BTU"): 3.96567,  # 1 Kilocalorie = 3.96567 BTU

("Electronvolts", "Kilocalories"): 1 / 2.6132e22,
("BTU", "Kilocalories"): 1 / 3.96567,
# Energy Conversions
("Electronvolts", "BTU"): 9.4782e-19,  # 1 Electronvolt = 9.4782 × 10^-19 BTU
("BTU", "Electronvolts"): 1 / 9.4782e-19,  # Reverse conversion

}

