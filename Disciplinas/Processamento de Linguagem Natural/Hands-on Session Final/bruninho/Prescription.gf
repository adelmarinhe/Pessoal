abstract Prescription = {
    flags
        startcat = Sentence ;

    cat
        Sentence ; Verb ; Medication; Amount ; Frequency ; Dosage;

    fun
        Have : Verb -> Dosage -> Frequency -> Sentence ;
        MedAmount : Amount -> Medication -> Dosage;
        Take, Use, Ingest : Verb ;
        Two, Three, Four, Five : Amount ;
        Med1, Med2, Med3, Med4 : Medication ;
        Once, Twice, Thrice: Frequency ;
}