/****** Object:  Table [dbo].[CDC_Covid19_Staff]    Script Date: 1/31/2021 4:49:51 AM ******/
USE [EchoAnalytics_Books]
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[CDC_Covid19_Staff](
	[OrgID] [nvarchar](50) NULL,
	[CollectionDate] [date] NULL,
	[NumStaffC19Died] [int] NULL,
	[ShortNurse] [nvarchar](50) NULL,
	[ShortClin] [nvarchar](50) NULL,
	[ShortAide] [nvarchar](50) NULL,
	[ShortOthStaff] [nvarchar](50) NULL,
	[NumStaffPosTest] [int] NULL,
	[NumStaffPosTestPosAg] [int] NULL,
	[NumStaffPosTestPosNaat] [int] NULL,
	[NumStaffPosTestPosAgNegNaat] [int] NULL,
	[NumStaffPosTestOther] [int] NULL,
	[NumStaffPosTestReInf] [int] NULL,
	[NumStaffPosTestReInfSymp] [int] NULL,
	[NumStaffPosTestReInfAsymp] [int] NULL,
	[NumStaffConfFlu] [int] NULL,
	[NumStaffOthResp] [int] NULL,
	[NumStaffConfFluC19] [int] NULL,
	[LoadDateTime] [datetime] NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[CDC_Covid19_Staff] ADD  CONSTRAINT [DF_CDC_Covid19_Staff_LoadDateTime]  DEFAULT (getdate()) FOR [LoadDateTime]
GO
