#### ubuntu 安装 docker

- 卸载旧的版本

  ```
  $ sudo apt-get remove docker docker-engine docker.io
  ```

  如果apt-get报告说没有安装这些软件包，那么就可以了。/var/lib/docker/目录会被保留。

- Trusty 14.04推荐额外套餐

  ```
  $ sudo apt-get update

  $ sudo apt-get install \
      linux-image-extra-$(uname -r) \
      linux-image-extra-virtual
      
  ```



3. 安装Docker ce 

   您可以根据需要以不同的方式安装Docker CE：

   - 大多数用户设置了Docker的存储库并从中安装，以方便安装和升级任务。 这是推荐的方法。
   - 一些用户下载DEB软件包并手动安装，并手动完成升级。 这在诸如在没有访问互联网的空隙系统上安装Docker的情况下是有用的。
   - 在测试和开发环境中，一些用户选择使用自动化便利脚本来安装Docker。

   ​

   **使用存储库进行安装**
   在首次在新的主机上安装Docker CE之前，需要设置Docker存储库。 之后，您可以从存储库安装和更新Docker。

   - [x] 设置报告

   1.   安装软件包以允许通过HTTPS使用存储库：

        ```
        $ sudo apt-get install \
            apt-transport-https \
            ca-certificates \
            curl \
            software-properties-common
        ```

   	2. 添加Docker的官方GPG密钥：

       ```
       $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
       ```

       通过搜索指纹的最后8个字符，验证您现在是否具有指纹键9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88。

       ```
       $ sudo apt-key fingerprint 0EBFCD88

       pub   4096R/0EBFCD88 2017-02-22
             Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
       uid                  Docker Release (CE deb) <docker@docker.com>
       sub   4096R/F273FCD8 2017-02-22
       ```

   	3. 使用以下命令设置稳定存储库。 您始终需要稳定的存储库，即使您想要从边缘或测试存储库安装构建。 要添加边缘或测试库，请在以下命令中的单词stable之后添加单词edge或测试（或两者）。

       > 注意：下面的lsb_release -cs子命令返回Ubuntu发行版的名称，例如xenial。 有时，在像Linux Mint这样的发行版中，您可能需要将$（lsb_release -cs）更改为您的父级Ubuntu发行版。 例如，如果您使用的是Linux Mint Rafaela，则可以使用可信赖的。

       **amd64**:

       ```
       $ sudo add-apt-repository \
          "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
          $(lsb_release -cs) \
          stable"

       ```

       **armhf**:

       ```
       $ sudo add-apt-repository \
          "deb [arch=armhf] https://download.docker.com/linux/ubuntu \
          $(lsb_release -cs) \
          stable"

       ```

       **s390x**:

       ```
       $ sudo add-apt-repository \
          "deb [arch=s390x] https://download.docker.com/linux/ubuntu \
          $(lsb_release -cs) \
          stable"
       ```

   - [x] 安装docker ce

   1. 更新 apt 到最新

      ```
      $ sudo apt-get update
      ```

   2. 安装最新版本的Docker CE，或转到下一步安装特定版本。 Docker的任何现有安装都被替换。

      ```
      $ sudo apt-get install docker-ce
      ```

   3. 在生产系统上，您应该安装特定版本的Docker CE，而不是始终使用最新版本。 此输出被截断。 列出可用的版本。

      ```
      $ apt-cache madison docker-ce
       docker-ce | 17.07.0~ce-0~ubuntu | https://download.docker.com/linux/ubuntu/ trusty/edge amd64 Packages
       docker-ce | 17.06.2~ce-0~ubuntu | https://download.docker.com/linux/ubuntu/ trusty/edge amd64 Packages
       docker-ce | 17.06.1~ce-0~ubuntu | https://download.docker.com/linux/ubuntu/ trusty/edge amd64 Packages
       docker-ce | 17.06.0~ce-0~ubuntu | https://download.docker.com/linux/ubuntu/ trusty/edge amd64 Packages
       docker-ce | 17.05.0~ce-0~ubuntu-trusty | https://download.docker.com/linux/ubuntu/ trusty/edge amd64 Packages
       docker-ce | 17.04.0~ce-0~ubuntu-trusty | https://download.docker.com/linux/ubuntu/ trusty/edge amd64 Packages
      ```

   4. 列表的内容取决于启用了哪些存储库。 选择要安装的特定版本。 第二列是版本字符串。 第三列是存储库名称，它指示软件包的存储库以及其稳定性级别。 要安装特定版本，请将版本字符串附加到包名称，并将其分隔一个等号（=）：

      ```
      $ sudo apt-get install docker-ce=<VERSION>
      ```

   5. ​