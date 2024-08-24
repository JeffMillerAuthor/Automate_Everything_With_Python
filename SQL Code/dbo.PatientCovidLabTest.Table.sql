USE [Automate_Everything_With_Python]

CREATE TABLE [dbo].[PatientCovidLabTest](
	[PatientID] [nvarchar](20) NULL,
	[PatientName] [nvarchar](75) NULL,
	[Results] [nvarchar](20) NULL,
	[Device_Identifier] [nvarchar](50) NULL,
	[Ordered_Test_Name] [nvarchar](150) NULL,
	[LOINC_Code] [nvarchar](20) NULL
) ON [PRIMARY]

