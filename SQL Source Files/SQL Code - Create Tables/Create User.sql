USE EchoAnalytics_Books
GO

CREATE LOGIN EchoUser WITH PASSWORD = '123'
GO

CREATE USER [EchoUser] FOR LOGIN [EchoUser]
GO

USE [EchoAnalytics_Books]
GO

ALTER ROLE [db_accessadmin] ADD MEMBER [EchoUser]
GO

USE [EchoAnalytics_Books]
GO

ALTER ROLE [db_datareader] ADD MEMBER [EchoUser]
GO

USE [EchoAnalytics_Books]
GO

ALTER ROLE [db_datawriter] ADD MEMBER [EchoUser]
GO
