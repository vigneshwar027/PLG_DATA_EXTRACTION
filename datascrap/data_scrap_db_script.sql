USE [master]
GO
/****** Object:  Database [DataScrapping]    Script Date: 11/4/2022 11:29:28 PM ******/
CREATE DATABASE [DataScrapping]
 
GO
USE [DataScrapping]
GO
/****** Object:  Table [dbo].[SourceUrl]    Script Date: 11/4/2022 11:29:29 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SourceUrl](
	[Item_Url] [nvarchar](max) NULL,
	[Category] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [DataScrapping] SET  READ_WRITE 
GO
