USE [Automate_Everything_With_Python]

CREATE TABLE [Automate_Everything_With_Python].[dbo].[Hospital](
	[ClinicID] [nvarchar](20) NULL,
	[ClinicName] [nvarchar](75) NULL,
	[City] [nvarchar](75) NULL,
	[State] [nvarchar](20) NULL,
	[Zip] [nvarchar](20) NULL)


INSERT [Automate_Everything_With_Python].[dbo].[Hospital] ([ClinicID], [ClinicName], [City], [State], [Zip]) VALUES ('79', 'Prosper Health Clinic', 'Plano', 'TX', '75025')
INSERT [Automate_Everything_With_Python].[dbo].[Hospital] ([ClinicID], [ClinicName], [City], [State], [Zip]) VALUES ('876', 'Legacy Health', 'Austin', 'TX', '78702')