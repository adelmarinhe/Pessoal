concrete MedicalPrescriptionEng of MedicalPrescription = open Prelude in {
  lincat
    Sentence, Verb, Medication, Amount, Frequency, Quantity, Dosage = SS ;

  lin
    Have verb dosage freq = {s = verb.s ++ dosage.s ++ freq.s} ;
    MedAmount amount med = {s = amount.s ++ Quantity.s ++ med.s} ;

    -- Verbs
    Take = {s = "Take"} ;
    Use = {s = "Use"} ;
    Ingest = {s = "Ingest"} ;

    -- Dosage
    NumberOfPills = {s = "doses of"} ;

    -- Amount
    One = {s = "one"} ;
    Two = {s = "two"} ;
    Three = {s = "three"} ;
    Four = {s = "four"} ;

    -- Medication
    Med1 = {s = "Acetaminophen"} ;
    Med2 = {s = "Omeprazole"} ;
    Med3 = {s = "Atorvastatin"} ;
    Med4 = {s = "Ibuprofen"} ;
    Med5 = {s = "Aspirin"} ;

    -- Frequency
    Once = {s = "once"} ;
    Twice = {s = "twice a day"} ;
    ThreeTimes = {s = "three times a day"} ;
    Daily = {s = "daily"} ;
    EveryMorning = {s = "every morning"} ;
    EveryEvening = {s = "every evening"} ;
    AfterBreakfast = {s = "after breakfast"} ;
    AfterLunch = {s = "after lunch"} ;
    AfterDinner = {s = "after dinner"} ;
}
