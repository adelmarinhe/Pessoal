abstract MedicalPrescription = {
  flags
    startcat = Sentence ;

  cat
    Sentence ; Verb ; Medication ; Amount ; Frequency ; Quantity ; Dosage ;

  fun
    Have : Verb -> Dosage -> Frequency -> Sentence ;
    MedAmount : Amount -> Medication -> Dosage ;
    Take, Use, Ingest : Verb ;
    NumberOfPills : Quantity ;
    One, Two, Three, Four : Amount ;
    Med1, Med2, Med3, Med4, Med5 : Medication ;
    Once, Twice, ThreeTimes, Daily : Frequency ;
    EveryMorning, EveryEvening : Frequency ;
    AfterBreakfast, AfterLunch, AfterDinner : Frequency ;
}
