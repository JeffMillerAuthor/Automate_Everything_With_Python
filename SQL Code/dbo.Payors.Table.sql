USE [Automate_Everything_With_Python]

CREATE TABLE [dbo].[Payors](
	[PayorID] [nvarchar](20) NOT NULL,
	[Payor] [nvarchar](75) NULL,
 CONSTRAINT [PK_Payor] PRIMARY KEY CLUSTERED 
(
	[PayorID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'1', N'SELF PAY')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'197', N'SELF PAY MEDICAID PENDING')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'200', N'BCBS PPO TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'203', N'BCBS FEDERAL TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'210', N'BCBS PRIMARY OUT OF STATE')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'230', N'COMMERCIAL AND INDEMNITY PLANS 1')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'235', N'COMMERCIAL AND INDEMNITY 2')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'300', N'BCBS HMO TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'303', N'AETNA HMO TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'306', N'CIGNA HMO TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'309', N'UNITED HEALTHCARE HMO TX')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'347', N'HUMANA PREFERRED TX')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'350', N'UNITED HEALTHCARE PPO TX')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'351', N'AETNA PPO TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'352', N'CIGNA PPO TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'357', N'BEECH STREET TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'361', N'PHCS PPO TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'383', N'HUMANA CHOICE CARE TX')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'394', N'UNITED HEALTHCARE OPTIONS PLUS TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'395', N'COVENTRY FIRST HEALTH TX')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'400', N'SECURE HORIZONS TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'401', N'MEDICARE MANAGEDCARE TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'404', N'HEALTHSPRINGS PPO')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'410', N'SECURE HORIZONS OTHER')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'411', N'HEALTHSMART PREFERRED')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'413', N'GEHA HEALTH PLANS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'450', N'MEDICAID MANAGEDCARE TX')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'452', N'MOLINA HEALTHCARE OF TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'480', N'TRICARE')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'482', N'TRICARE PRIME')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'501', N'MEDICARE TEXAS')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'511', N'MEDICARE TEXAS SECONDARY')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'520', N'MEDICARE RAILROAD')
INSERT [dbo].[Payors] ([PayorID], [Payor]) VALUES (N'550', N'MEDICAID TEXAS')

