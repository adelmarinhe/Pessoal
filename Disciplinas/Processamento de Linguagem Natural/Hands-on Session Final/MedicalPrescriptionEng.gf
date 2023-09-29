--gr -number=10 | l

concrete MedicalPrescriptionEng of MedicalPrescription = open Prelude in {
  param
  Number = Sg | Pl ;

  lincat
    Sentence, Verb, Medication, Frequency, Peposition, TimePeriod, Dosage = SS ;
    Quantity = {s : Number => Str} ;
    Amount = {s : Str ; n : Number} ;

    oper
    det : Number -> Str -> {s : Str ; n : Number} =
    \n,d -> {
        s = d ;
        n = n
    } ;

    noun : Str -> Str -> {s : Number => Str} =
    \car,cars -> {s = table { Sg => car ; Pl => cars } } ;

    regNoun : Str -> {s : Number => Str} =
    \car -> noun car (car + "s") ;

  lin
    Phrase verb amount quantity prep med freq timeperiod = { s = verb.s ++ amount.s ++ quantity.s ! amount.n ++ prep.s ++ med.s ++ freq.s ++ timeperiod.s } ;

    -- Verbs
    Take = {s = "Take"} ;
    Ingest = {s = "Ingest"} ;
    -- Inject = {s = "Inject"} ;

    -- Peposition
    Of = ss "of" ;

    -- Quantity
    Dose = regNoun "dose" ;

    -- Amount
    One = det Sg "one" ;
    Two = det Pl "two" ;
    Three = det Pl "three" ;
    Four = det Pl "four" ;

    -- Medication: based on the 10 most consumed worldwide
    Med1 = {s = "Acetaminophen"} ;
    Med2 = {s = "Aspirin"} ;
    Med3 = {s = "Ibuprofen"} ;
    Med4 = {s = "Lisinopril (Prinivil, Zestril)"} ;
    Med5 = {s = "Atorvastatin (Lipitor)"} ;
    Med6 = {s = "Levothyroxine (Synthroid)"} ;
    Med7 = {s = "Metformin (Glucophage)"} ;
    Med8 = {s = "Amlodipine (Norvasc)"} ;
    Med9 = {s = "Omeprazole (Prilosec)"} ;
    Med10 = {s = "Hydrochlorothiazide (Microzide)"} ;

    -- Frequency
    Once = { s = "once a day" };
    Twice = { s = "twice a day" } ;
    ThreeTimes = { s = "three times a day" } ;
    FourTimes = { s = "four times a day" } ;
    EverySixHours = {s = "every six hours"} ;
    EveryEightHours = {s = "every eight hours"} ;

    -- Time Period
    Daily = {s = "every day"} ;
    ForAWeek = {s = "for a week"} ;
}
