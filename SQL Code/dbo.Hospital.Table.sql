USE [Automate_Everything_With_Python]

CREATE TABLE [dbo].[Hospital](
	[ClinicID] [nvarchar](20) NOT NULL,
	[ClinicName] [nvarchar](75) NULL,
	[City] [nvarchar](75) NULL,
	[State] [nvarchar](20) NULL,
	[Zip] [nvarchar](20) NULL,
 CONSTRAINT [PK_Hospital] PRIMARY KEY CLUSTERED 
(
	[ClinicID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

