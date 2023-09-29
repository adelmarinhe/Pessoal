concrete PrescriptionEng of Prescription = open Prelude in {
lincat
    Sentence, Verb, Medication, Amount, Frequency = SS ;
lin
    Have verb dosage freq = 
        {s = verb.s ++ dosage.s ++ freq.s} ;
    MedAmount amount med = 
        {s = amount.s ++ "doses of" ++ med.s} ;
    Take = ss "take" ;
    Use = ss "use" ;
    Ingest = ss "ingest" ;
    Two = ss "two" ;
    Three = ss "three" ;
    Four = ss "four" ;
    Five = ss "five" ;
    Med1 = ss "Acetaminophen" ;
    Med2 = ss "Omeprazole" ;
    Med3 = ss "Atorvastatin" ;
    Med4 = ss "Ibuprofen" ;
    Once = ss "daily" ;
    Twice = ss "two times a day" ;
    Thrice = ss "three times a day" ;
}