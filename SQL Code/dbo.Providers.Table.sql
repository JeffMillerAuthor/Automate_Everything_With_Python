USE [Automate_Everything_With_Python]

CREATE TABLE [dbo].[Providers](
	[ProviderID] [nvarchar](20) NOT NULL,
	[ProviderName] [nvarchar](75) NULL,
	[Phone] [nvarchar](20) NULL,
 CONSTRAINT [PK_Provider] PRIMARY KEY CLUSTERED 
(
	[ProviderID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

INSERT [dbo].[Providers] ([ProviderID], [ProviderName], [Phone]) VALUES (N'6015', N'Baker, Sara', N'385-555-0145')
INSERT [dbo].[Providers] ([ProviderID], [ProviderName], [Phone]) VALUES (N'6350', N'Zhou, Jon', N'688-555-0128')
INSERT [dbo].[Providers] ([ProviderID], [ProviderName], [Phone]) VALUES (N'6541', N'Carson, Kevin', N'477-555-0181')
