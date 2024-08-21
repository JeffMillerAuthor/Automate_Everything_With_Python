USE [Automate_Everything_With_Python]

CREATE TABLE [dbo].[PatientAssessments](
	[PostPeriod] [nvarchar](20) NULL,
	[DateEntered] [datetime] NULL,
	[ProviderID] [nvarchar](20) NULL,
	[ClinicID] [nvarchar](20) NULL,
	[DateTimeAssessment] [datetime] NULL,
	[PatientID] [nvarchar](20) NULL,
	[PatientName] [nvarchar](75) NULL,
	[Temperature] [decimal](18, 1) NULL,
	[Pulse_Oximeter] [int] NULL,
	[SOB] [nvarchar](20) NULL,
	[Cough] [nvarchar](20) NULL,
	[Abdominal_Pain] [nvarchar](20) NULL,
	[Diarrhea_Or_Other_Gi_Upset] [nvarchar](20) NULL,
	[Nausea] [nvarchar](20) NULL,
	[Loss_Of_Taste] [nvarchar](20) NULL,
	[Red_Shadowed_Eyes_Or_Pink_Eye] [nvarchar](20) NULL,
	[Tingling_Sensation_Of_Face_Or_Hands] [nvarchar](20) NULL,
	[Sore_Throat] [nvarchar](20) NULL,
	[Chills_And_Or_Repeated_Shaking_With_Chills] [nvarchar](20) NULL,
	[Muscle_Pain] [nvarchar](20) NULL,
	[Loss_Of_Smell] [nvarchar](20) NULL,
	[Headache] [nvarchar](20) NULL
) ON [PRIMARY]
