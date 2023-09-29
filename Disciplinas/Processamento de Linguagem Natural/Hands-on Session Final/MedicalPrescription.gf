abstract MedicalPrescription = {
  flags
    startcat = Sentence ;

  cat
    Sentence ; Verb ; Medication ; Amount ; Frequency ; TimePeriod ; Quantity ; Peposition ;

  fun
    Phrase : Verb -> Amount -> Quantity -> Peposition -> Medication -> Frequency -> TimePeriod -> Sentence ;

    Take, Ingest : Verb ;
    Dose : Quantity ;
    Of : Peposition ;
    One, Two, Three, Four : Amount ;
    Med1, Med2, Med3, Med4, Med5, Med6, Med7, Med8, Med9, Med10 : Medication ;
    Once, Twice, ThreeTimes, EverySixHours, EveryEightHours : Frequency ;
    Daily, ForAWeek : TimePeriod ;
}
