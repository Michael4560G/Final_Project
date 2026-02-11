import os
import re

def comprehensive_vehicle_audit(folder_path):
    # הרשימה המלאה שלך (קיצרתי כאן לתצוגה, תשתמש ברשימה המלאה שבקוד שלך)
    brands = [
        "9ff", "Abadal", "Abarth", "Abbott-Detroit", "ABT", "AC", "Acura", "Adly", "Aeon", "Aermacchi", "Aiways", "Aixam", "AJS", "Alfa Romeo", "Alpina", "Alpine", "Alta", "Alvis", "AMC", "Amilcar", "Ampere", "Ankai", "Apollo", "Apperson", "Aprilia", "Arash", "Arcfox", "Ariel", "ARO", "Arrinera", "Arrival", "Artega", "Ascari", "Askam", "Aspark", "Aston Martin", "Atalanta", "Auburn", "Audi", "Audi Sport", "Austin", "Austin-Healey", "Autobacs", "Autobianchi", "Avatr", "Axon",
        "BAC", "BAIC", "Bajaj", "Baojun", "Baotian", "Barkas", "Barrow", "Beiben", "Benda", "Benelli", "Bentley", "Berkeley", "Berliet", "Bertone", "Bestune", "Beta", "BharatBenz", "Bimota", "Bitter", "Bizzarrini", "Blitz", "BMW", "BMW M", "BMW Motorrad", "Borgward", "Bowler", "Brabus", "Brammo", "Bridgestone", "Brilliance", "Bristol", "Brixton", "Brooke", "Brough Superior", "BSA", "Bufori", "Bugatti", "Buick", "Bultaco", "BYD", "Byton",
        "Cadillac", "Cagiva", "CAMC", "Can-Am", "Canoo", "Caparo", "Carlsson", "Casalini", "Caterham", "CFMoto", "Changan", "Changfeng", "Changhe", "Checkered Flag", "Checker", "Chery", "Chevrolet", "Chrysler", "Cisitalia", "Citroen", "Cizeta", "Cole", "Corvette", "Cupra", "Cushman", "Czinger",
        "Dacia", "Dadi", "Daelim", "Daewoo", "DAF", "Daihatsu", "Daimler", "Dallara", "Dartz", "Datsun", "David Brown", "Dayun", "De Tomaso", "Deepal", "Delage", "Delahaye", "DeLorean", "Derbi", "DeSoto", "Detroit Electric", "Devel Sixteen", "Diatto", "DINA", "DKW", "DMC", "Dodge", "Dongfeng", "Donkervoort", "Drako", "DS", "Ducati", "Duesenberg", "Dutton",
        "Eagle", "EDAG", "Edsel", "Eicher", "Elaris", "Electric Leopard", "Elemental", "Elfin", "Elva", "Energica", "Englon", "Enovate", "ERF", "Eterniti", "EVEasy", "Exeed",
        "Facel Vega", "Fantic", "Faraday Future", "FAW", "Ferrari", "Fiat", "Fisker", "Foden", "Force Motors", "Ford", "Forthing", "Foton", "FPV", "Franklin", "Freightliner", "FSO", "Fuso",
        "GAC", "Gardner Douglas", "GasGas", "GAZ", "Geely", "Genesis", "Geo", "Geometry", "Gilbern", "Gilera", "Gillet", "Ginetta", "GMC", "Gnome", "Gogoro", "Golden Dragon", "Gonow", "Govecs", "Great Wall", "Grinnall", "Grumman", "Gullwing", "Gumpert", "GWM",
        "Hafei", "Haima", "Hanomag", "Harley-Davidson", "Hartge", "Haval", "Hawtai", "Healey", "Heinkel", "Hennessey", "Hercules", "Higer", "Hillman", "Hindustan", "Hino", "HiPhi", "Hispano-Suiza", "Holden", "Hommell", "Honda", "Hongqi", "Horch", "Hotchkiss", "HRE", "HSV", "Hudson", "Hummer", "Hupmobile", "Husaberg", "Husqvarna", "Hyosung", "Hyundai",
        "IC Bus", "IKCO", "IM Motors", "Imperial", "Indian", "Infiniti", "Innocenti", "Innoson", "Intermeccanica", "International", "Invicta", "Irmscher", "Isdera", "Isuzu", "Italdesign", "Italjet", "Iveco", "Izh",
        "JAC", "Jaecoo", "Jaguar", "Jawa", "JBA", "Jeep", "Jensen", "Jiefang", "Jinbei", "JMC", "Jordan", "Jowett",
        "Kalmar", "Karma", "Karsan", "Kawasaki", "Keeway", "Kenworth", "KGM", "Kia", "Kish Khodro", "Kissel", "Kodiak", "Koenigsegg", "Kove", "KTM", "Kymco",
        "Lada", "Lagonda", "Lamborghini", "Lambretta", "Lanchester", "Lancia", "Land Rover", "Landwind", "Lantana", "Laraki", "LaSalle", "Laval", "Laverda", "Laxman", "Lazareth", "Leapmotor", "Lecson", "Lenco", "Lexus", "Leyland", "Lifan", "Ligier", "Lincoln", "Lister", "Lloyd", "Local Motors", "Lola", "London EV Company", "Lorinser", "Lotec", "Lotus", "LTI", "Lucid", "Luxgen", "Lynk & Co",
        "Mack", "Magirus", "Mahindra", "Maico", "Malaguti", "MAN", "Mansory", "Marcos", "Marlin", "Marmon", "Marseilles", "Marussia", "Maruti", "Maserati", "Mastretta", "Matra", "Maxus", "Maybach", "Mazda", "Mazzanti", "McLaren", "Mega", "Melex", "Melkus", "Mercedes", "Mercedes-Benz", "Mercury", "Merkur", "Metrocab", "MG", "Microcar", "Militem", "Mini", "Mitsubishi", "Mitsuoka", "Moke", "Mondial", "Monteverdi", "Morgan", "Morris", "Mosler", "Moto Guzzi", "Motus", "MTM", "Munch", "MV Agusta", "MVM",
        "Nacional", "Nardi", "Nash", "Navistar", "NAZ", "Naza", "Neoplan", "NextEV", "NIM", "Nio", "Nissan", "Noble", "Norton", "NSU", "Nyobolt",
        "Oldsmobile", "Oltcit", "Omoda", "Opel", "Ora", "Orca", "Osella", "Oshkosh", "Overland",
        "Packard", "Pagani", "Panoz", "Panther", "Paton", "Peerless", "Pegaso", "Perodua", "Peterbilt", "Peugeot", "PGO", "Piaggio", "Pierce-Arrow", "Pininfarina", "Plymouth", "Polestar", "Pontiac", "Porsche", "Praga", "Premier", "Proton", "Puch", "Puma",
        "QJ Motor", "Qoros", "Quant", "Quattro",
        "Radical", "Ram", "Rambler", "Range Rover", "Ranz", "Rapel", "Ravon", "Ree", "Reliant", "Renaissance", "Renault", "Renault Samsung", "Reo", "Rezvani", "Rieju", "Rimac", "Rinspeed", "Rivian", "Roewe", "Rolls-Royce", "Ronart", "Rossion", "Rover", "Royal Enfield", "Ruf",
        "Saab", "SAIC", "Saleen", "Sanyang", "Saturn", "Scania", "Scion", "Scomadi", "Sconset", "Scout", "Seat", "Seres", "Shelby", "Sherco", "Shineray", "Siam", "Sisu", "Skoda", "Skywell", "Skyworth", "Smart", "Smit", "SMS", "Solaris", "Soltera", "Sono", "Soueast", "Spectre", "Spyker", "SRT", "SsangYong", "SSC", "Standard", "Stealth", "Steeda", "Steyr", "Studebaker", "Stutz", "Subaru", "Sunbeam", "Super Soco", "Sur-Ron", "Suzuki", "SWM", "SYM",
        "Talaria", "Talbot", "TAMA", "Tamo", "Tank", "Taro", "Tata", "Tatra", "Tazzari", "TechArt", "Tesla", "Thai Rung", "Think", "Thomas", "Tofas", "Togg", "Toleman", "Tollman", "Tomahawk", "Tomos", "Tork", "Toyota", "Trabant", "Tramontana", "Triumph", "Troller", "TVR", "TVS", "Tyrrell",
        "UAZ", "UD", "UF", "Ultima", "Unic", "Unimog", "Unity", "Ural",
        "Vanderhall", "Vanwall", "Vauxhall", "Vector", "Veldhuis", "Vence", "Vento", "Venturi", "Vespa", "Victory", "Viglietti", "Vigo", "Vinal", "VinFast", "Vision", "VLF", "Voge", "Volkswagen", "Volvo", "Vortec", "Vortex", "Voskhod", "Voyah", "Vuhl",
        "W Motors", "Waker", "Wald", "Waltham", "Wartburg", "Weld", "Westfield", "Wey", "Wiesmann", "Willys", "Wolseley", "Workhorse", "Wuling",
        "Xenia", "Xingchi", "Xinghai", "XPeng", "Xra",
        "Yamaha", "Yaris", "Yema", "Yes!", "Yugo", "Yutong",
        "ZAG", "Zagato", "Zamyad", "Zastava", "ZAZ", "Zeekr", "Zender", "Zenvo", "Zero", "ZhiDou", "Zhonghua", "Zotye", "Zundapp", "Zut", "ZXV", "Zytek"
    ]

    target_brands = sorted(list(set(brands)))

    try:
        # סינון לקבצי PNG בלבד כבר בשלב הקריאה
        raw_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
    except Exception as e:
        print(f"שגיאה בגישה לתיקייה: {e}")
        return

    def normalize(text):
        # הופך לקטן ומסיר כל מה שאינו אות או מספר
        return re.sub(r'[^a-z0-9]', '', text.lower())

    # מיפוי שמות הקבצים (ללא הסיומת) לאחר נרמול
    normalized_png_files = {}
    for f in raw_files:
        name_without_ext = os.path.splitext(f)[0]
        normalized_png_files[normalize(name_only := name_without_ext)] = f

    found = []
    missing = []

    for brand in target_brands:
        brand_norm = normalize(brand)
        
        # בדיקה 1: התאמה מדויקת (הכי בטוח)
        if brand_norm in normalized_png_files:
            found.append((brand, normalized_png_files[brand_norm]))
        else:
            # בדיקה 2: האם שם המותג מוכל בתוך שם קובץ כלשהו (למשל "toyota" בתוך "toyota_logo")
            match = None
            for f_norm, original_name in normalized_png_files.items():
                if brand_norm in f_norm:
                    match = original_name
                    break
            
            if match:
                found.append((brand, match))
            else:
                missing.append(brand)

    # הדפסת התוצאות
    print("\n" + "="*70)
    print(f"🏁 דוח סריקת לוגואים - קבצי PNG בלבד")
    print("="*70)
    print(f"✅ לוגואים שנמצאו: {len(found)}")
    print(f"❌ לוגואים חסרים: {len(missing)}")
    print(f"📈 אחוז כיסוי: {len(found)/len(target_brands):.1%}")
    print("-" * 70)

    if missing:
        print("\n🔍 רשימת ה-PNG החסרים:")
        for i in range(0, len(missing), 4):
            row = missing[i:i+4]
            print("{:<17} {:<17} {:<17} {:<17}".format(*(row + [""] * (4 - len(row)))))
    else:
        print("\n🎉 מושלם! כל המותגים נמצאו כקבצי PNG.")

# הרץ עם הנתיב שלך
my_path = r"/Users/mymac/Desktop/Data science/שנה ג/פרויקט גמר/מסכים/html5up-helios/Final_Project/logos/original/"
comprehensive_vehicle_audit(my_path)