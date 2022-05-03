function (doc) {
  emit(doc.city, [1,doc.properties.number_of_jobs_000_persons_2018_19,doc.properties.median_employment_income_per_job_persons_2018_19]);
}