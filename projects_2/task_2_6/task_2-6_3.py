donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()

if donor == "I":
    print(f"\n Донор с группой {donor} может давать кровь пациенту с группой {recipient}")
    
elif donor == recipient:
    print(f"\n Донор с группой {donor} может давать кровь пациенту с группой {recipient}")
    
elif donor == "II" and (recipient == "II" or recipient == "IV"):
    print(f"\n Донор с группой {donor} может давать кровь пациенту с группой {recipient}")
    
elif donor == "III" and (recipient == "III" or recipient == "IV"):
    print(f"\n Донор с группой {donor} может давать кровь пациенту с группой {recipient}")
    
elif donor == "IV" and recipient == "IV":
    print(f"\n Донор с группой {donor} может давать кровь пациенту с группой {recipient}")
    
else:
    print(f"\n Донор с группой {donor} НЕ может давать кровь пациенту с группой {recipient}")