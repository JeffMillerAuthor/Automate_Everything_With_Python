/****** Script for SelectTopNRows command from SSMS  ******/
SELECT p.ProviderID
	  ,p.ProviderName
	  ,p.Phone
      ,pa.ClinicID
      ,pa.PatientID
      ,pa.PatientName
      ,pa.Temperature
      ,pa.Pulse_Oximeter
	  ,pa.DateTimeAssessment 
FROM Automate_Everything_With_Python.dbo.PatientAssessments pa
	left join Automate_Everything_With_Python.dbo.Providers p on pa.ProviderID = p.ProviderID
--WHERE pa.Temperature >= 100
--	and pa.Pulse_Oximeter < 98


SELECT p.ProviderID,
       p.ProviderName,
       p.Phone,
       pa.ClinicID,
       pa.PatientID,
       pa.PatientName,
       pa.Temperature,
       pa.Pulse_Oximeter,
       pa.DateTimeAssessment 
FROM Automate_Everything_With_Python.dbo.PatientAssessments pa
LEFT JOIN Automate_Everything_With_Python.dbo.Providers p ON pa.ProviderID = p.ProviderID
WHERE pa.Temperature >= 100
AND pa.Pulse_Oximeter < 98
AND pa.DateTimeAssessment = (
    SELECT MAX(pa2.DateTimeAssessment)
    FROM Automate_Everything_With_Python.dbo.PatientAssessments pa2
    WHERE pa.PatientID = pa2.PatientID)
