# 计算概论作业4

## 作业、进程、线程

### 解释作业、进程、线程的概念

***

#### 1.作业
   
  用户在一个事务处理过程中要求计算机系统所做的工作的集合。
  
  它包括用户程序、所需要的数据集控制命令等，由一系列有序的步骤组成的。
  
#### 2.进程

  进程是表示资源分配的基本单位，又是调度运行的基本单位。
  
  例如，用户运行自己的程序，系统就创建一个进程，并为它分配资源，
  
  包括各种表格、内存空间、磁盘空间、I/O设备等。
  
  然后，把该进程放人进程的就绪队列。
  
  进程调度程序选中它，为它分配CPU以及其它有关资源，该进程才真正运行。
  
  然而，在Mac、Windows NT等采用微内核结构的操作系统中，进程的功能发生了变化：
  
  它只是资源分配的单位，而不再是调度运行的单位。
  
  #### 3.线程（线程是进程中执行运算的最小单位，亦即执行处理机调度的基本单位）
  
  随着计算机的发展，对CPU的要求越来越高，进程之间的切换开销较大，已经无法满足越来越复杂的程序的要求了。
  
  于是就发明了线程，线程是程序执行中一个单一的顺序控制流程，是程序执行流的最小单元，是处理器调度和分派的基本单位。
  
  一个进程可以有一个或多个线程，各个线程之间共享程序的内存空间(也就是所在进程的内存空间)。
  
  一个标准的线程由线程ID、当前指令指针(PC)、寄存器和堆栈组成。
  
  而进程由内存空间(代码、数据、进程空间、打开的文件)和一个或多个线程组成。
  

### 进程和线程概念的提出分别解决了什么问题？

***

#### 1.进程解决的问题——并发执行，实现交互

当计算机由批处理模式进入交互模式时，程序员希望计算机能及时响应交互，

这需要计算机能同时完成多个作业（并发执行程序）才可能实现。

程序员们采用时间片的方法解决了这个问题，也就是将时间分为若干个时间片，每个时间片之内处理一个作业。

这就需要作业之间的切换。

为了实现作业的切换，提出了进程概念。

对每个作业，计算机创建若干个进程，创建好后，进程进入就绪序列，处于Ready状态。

分到时间片后进程就可以运行，时间片用完，又恢复到Ready状态或者Exit状态。

这样就可以通过切换进程实现切换作业实现交互模式。

#### 2.线程解决的问题——减少并发执行时的时空开销

在操作系统中引入进程实现了多个程序并发执行，改善了资源利用率、提高了系统的吞吐量；

在操作系统中再引入线程是为了减少程序并发执行时所付出的时空开销，使操作系统具有更好的并发性。

为了说明这一点，我们首先回顾进程的两个基本属性：

```

(1)进程是一个可拥有资源的独立单位；

(2)进程同时又是——个可以独立调度和分派的基本单位。

```

正是由于进程具有这两个基本属性，才使之成为一个能独立运行的基本单位，从而也就构成了进程并发执行的基础。

然而为使程序能并发执行，系统还必须进行以下的一系列操作：

```

(1)创建进程。系统在创建进程时，必须为之分配其所必需的、除处理机以外的所有资源。如内存空间、I／0设备以及建立相应的PCB。

(2)撤消进程。系统在撤消进程时，又必须先对这些资源进行回收操作，然后再撤消PCB。

(3)进程切换。在对进程进行切换时，由于要保留当前进程的CPU环境和设置新选中进程的CPU环境，为此需花费不少处理机时间。

```

简言之，由于进程是一个资源拥有者，因而在进程的创建、撤消和切换中，系统必须为之付出较大的时空开销。

也正因为如此，在系统中所设置的进程数目不宜过多，进程切换的频率也不宜太高，但这也就限制了并发程度的进一步提高。

引入线程后，线程作为调度和分派的基本单位，而不作为独立分配资源的单位，这使得线程可以轻装运行；

而且对拥有资源的基本单位，可以不频繁地对之进行切换，这样就可以进一步减少切换过程中的时空开销，使操作系统有更好的并发性。

## 虚拟存储器

### 1.虚拟存储器的概念

>virtual memory (also virtual storage) is a memory management technique that provides an "idealized abstraction of the storage resources that are actually available on a given machine"[1] which "creates the illusion to users of a very large (main) memory.(Wikipedia)

虚拟内存是一种内存管理技术，它能提供“在给定计算机上实际可用的储存资源的一种理想化的抽象”，创造一种使用户感觉储存空间很大的一种假象。

### 2.虚拟存储器的工作原理

①中央处理器访问主存的逻辑地址分解成组号a和组内地址b，并对组号a进行地址变换，即将逻辑组号a作为索引，查地址变换表，以确定该组信息是否存放在主存内。

②如该组号已在主存内，则转而执行④；如果该组号不在主存内，则检查主存中是否有空闲区，如果没有，便将某个暂时不用的组调出送往虚拟存储器，以便将这组信息调入主存。

③从虚拟存储器读出所要的组，并送到主存空闲区，然后将那个空闲的物理组号a和逻辑组号a登录在地址变换表中。

④从地址变换表读出与逻辑组号a对应的物理组号a。

⑤从物理组号a和组内字节地址b得到物理地址。

⑥根据物理地址从主存中存取必要的信息。

### 3.虚拟存储器的作用

* 1.由于内存隔离而提高安全性，

* 2.使用分页技术在概念上使用比物理上可用的内存更多的内存。

















