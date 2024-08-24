USE [Automate_Everything_With_Python]

CREATE TABLE [dbo].[PatientBiographics](
	[PatientID] [nvarchar](20) NOT NULL,
	[PatientName] [nvarchar](75) NULL,
	[BirthDate] [date] NULL,
	[MaritalStatus] [nvarchar](20) NULL,
	[Race] [nvarchar](20) NULL,
	[Gender] [nvarchar](20) NULL,
	[Phone] [nvarchar](20) NULL,
	[InsuranceID] [nvarchar](20) NULL,
 CONSTRAINT [PK_Patient] PRIMARY KEY CLUSTERED 
(
	[PatientID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

