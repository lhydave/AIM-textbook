# 《AI 中的数学》教科书

本仓库包含《AI 中的数学》教科书的源代码、图像文件和 pdf 文件。

## 查看和下载最新版的 pdf 文件

如果你只是想查看本书的 pdf 文件，可以点击[这里](https://github.com/lhydave/AIM-textbook/blob/master/main.pdf)，你将看到本书的最新版本。

如果你想下载本书的 pdf，在点击之后，点击下图中的按钮即可下载。

![image](readme-img/download-pdf.png)

## 下载本书的源代码

你可以下载本书的源代码，然后自己编译本书。有以下几种方式可以下载本书的源代码。注意，如果你希望修改本书的源代码，并将这一修改重新提交回本仓库，请使用第二种或第三种方式，第一种方式可能无法提交修改。

### 下载压缩包

可以按照下图所示的方法下载本书源代码的压缩包，即在本页面上点击“Code”按钮，然后点击“Download ZIP”按钮。

![image](readme-img/download-zip.png)

如果你想下载本书的源代码（例如，你想自己编译本书或者修复错误），可以点击下图中的按钮。

### 使用 GitHub Desktop

你可以使用 GitHub Desktop 来克隆本仓库，从而下载本书的源代码。首先，你可以通过[这个链接](https://github.com/apps/desktop)来下载 GitHub Desktop。然后，在 GitHub Desktop 中，根据提示，登录你的 GitHub 账号（如果没有请先创建账号）。你可以按照下列步骤来克隆本仓库。

1. 在 GitHub 的网页上点击“Code”按钮，然后点击“Open with GitHub Desktop”按钮，如下图所示，GitHub Desktop 会自动打开。

![image](readme-img/download-desktop-1.png)

2. 在 GitHub Desktop 中，选择本仓库的保存路径，然后点击“Clone”按钮。

![image](readme-img/download-desktop-2.png)

### 使用 Git 命令行工具

你也可以使用 Git 命令行工具来克隆本仓库。首先，你需要安装 Git 命令行工具，你可以通过[官网](https://git-scm.com/downloads)下载并安装。安装完成后，打开命令行工具，输入以下命令来克隆本仓库：

    ```bash
    git clone https://github.com/lhydave/AIM-textbook.git
    ```

## 在本地编译本书

如果你希望在本地编译本书以生成 PDF 格式的电子书，你需要安装一些必要的工具。以下是详细的步骤：

### 安装 $\LaTeX$

本书使用 $\LaTeX$ 进行排版，因此你需要安装 $\LaTeX$。你可以通过[官网](https://www.latex-project.org/get/#tex-distributions)来安装 $\LaTeX$。

### 编译本书

有很多方式可以编译本书，你可以使用图形化的 $\LaTeX$ 编辑器，也可以使用命令行工具。因为不同的图形化 $\LaTeX$ 编辑器操作方式不同，这里只介绍命令行工具的使用方法。

1. 首先，在命令行中进入本书的根目录。

2. 然后，运行以下命令：
```bash
latexmk main.tex --xelatex
```

3. 等待编译完成，你就可以在 `main.pdf` 中看到本书的内容了。

## 向本书提出勘误和修改提议

如果你发现本书中的错误，或者有更好的写作或修改建议，欢迎提出。由于本书采用 GitHub 仓库的模式进行管理，你可以通过 Issue 和 Pull Request 两种方式提出勘误和修改提议。

### 通过 Issue 提出勘误和修改提议

*在使用 Issue 提交建议之前，请仔细查阅 [Issue 规范](issue-format.md)，否则你的 Issue 可能会被忽略或关闭。*

1. 在本网页中，点击 `Issues` 标签。
2. 点击 `New issue` 按钮。

![image](readme-img/issue-1.png)

3. 在 `Title` 中输入勘误或修改提议的标题。
4. 在 `Write` 中输入勘误或修改提议的详细内容，请具体到章节和页码，可以附上图片，数学请使用 $\LaTeX$ 公式。
5. 点击 `Submit new issue` 按钮。

![image](readme-img/issue-2.png)

## 通过 Pull Request 提交勘误和修改提议

使用 Pull Request 提交勘误和修改提议，可以直接修改源代码，因此是一种更加直接的方式。不过 Pull Request 有相对复杂的流程，我们这里不展开介绍。有需要的读者可以参阅[这篇博客](https://blog.csdn.net/m0_62993379/article/details/144177777)。

也欢迎大家通过 Pull Request 来修复其他人在 Issue 中提出的问题，这种情况下，请引用一下对应的 Issue 编号。