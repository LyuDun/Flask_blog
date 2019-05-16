# 数据结构的标准形式（C、Python版本）：2.链表
<!-- TOC -->
- [一：单链表](#一：单链表)
- [1. 定义](#1-定义)        
- [2.初始化](#2初始化)
- [3.判空](#3判空)
- [4.求表长](#4求表长)
- [5.按序号查找](#5按序号查找)
- [6.按值查找](#6按值查找)
- [8.在第i个位置插入e](#8在第i个位置插入e)
- [9.头插](#9头插)
- [10.尾插](#10尾插)
- [11.头插建立链表](#11头插建立链表)
- [12.尾插建立链表](#12尾插建立链表)
- [13.删除节点](#13删除节点)
- [14.打印节点](#14打印节点)
- [15.销毁节点](#15销毁节点)
- [16.翻转链表](#16翻转链表)
- [17.不遍历链表删除非尾节点](#17不遍历链表删除非尾节点)
- [18.遍历一次找到中间节点](#18遍历一次找到中间节点)        -
- [19.遍历一遍，找到倒数第k个节点(k从1开始)](#19遍历一遍找到倒数第k个节点k从1开始)
- [20.冒泡排序](#20冒泡排序)
- [21.插入排序](#21插入排序)
- [22.快速排序](#22.快速排序)
- [23.合并两个有序链表](#23.合并两个有序链表)
- [24.判断链表是否有环，如果有环，求长度和入口](#24.判断链表是否有环，如果有环，求长度和入口)
- [二：Python实现链表](#二：Python实现链表)
<!-- /TOC -->

## 一：单链表

- 初始化链表头部指针会用到二级指针或者一级指针的引用
- 销毁链表会用到二级指针或者一级指针的引用
- 插入、遍历、删除、清空用一级指针即可
- 定义成指针用 ->, 未定义为指针用 . 

  
### 1. 定义

```C
typedef struct Lnode{
    int data;
    struct Lnode *next;
}Lnode, *LinkList;
```

### 2.初始化

```C
int InitList(LinkList *L){
    *L = (LinkList)malloc(sizeof(LNode));
    if( !(L) ){
        print("Init Error");
        return False;
    }
    (*L)->next = NULL;
    return True;
}
```

### 3.判空

```C
bool Empty(LinkList L){
    if(L->next == NULL){
        return True;
    }else{
        return False;
    }
}
```

### 4.求表长

```C
int Length(LinkList L){
    int len = 0;
    LNode *p;
    p = L->next;
    if(L->next == NULL){
        return len;
    }
    while(L->next != NULL){
        p = p->next;
        len++;
    }
    return len;
}
```

### 5.按序号查找
```C
Lnode *GetElem(LinkList L, int i){
    int j = 1;
    Lnode *p = L->next;
    if(i == 0){
        return L;
    }
    if(i < 1){
        return L;
    }
    while(p->next != NULL && j < i){
        p = p->next;
        j++;
    }
    return p;
}
```

### 6.按值查找
```C
int LocateElem(LinkList L, int e){
    Lnode *p = L->next;
    int i = 1;
    if(Empty(L)){
        printf("Empty!\n")；
        return false;
    }
    while(p != NULL && p->data != e){
        p = p->next;
        i++;
    }
    return i;
}
```

### 8.在第i个位置插入e

```C
LinkList ListInsert(LinkList L, int i, int e){
    LNode *p;
    LNode *s;
    p = GetElem(i);
    s = (LinkList)malloc(sizeof(LNode));
    s->data = e;
    s->next = p->next;
    p->next = s;
    return L;
}
```

### 9.头插

```C
LinkList HeadInset(LinkList L, int e){
    LNode *s;
    s = (LinkList)malloc(sizeof(LNode));
    s->data = e;
    s->next = L->next;
    L->next = s;
    return L;
}
```

### 10.尾插

```C
LinkList TailInsert(LinkList L, int e){
    LNode  *s, *p = L->next;
    s = (LinkList)malloc(sizeof(LNode));
    s->data = e;
    while(*p->next != NULL){
        p->next = s;
    }
    s->next = NULL;
    return L;
}
```

### 11.头插建立链表

```C
LinkList HeadCreateList(LinkList &L, int a[], int n){
    L = (LinkList)malloc(sizeof(LNode));
    L->next = NULL;
    LNode *s;
    fro(int i = 0; i < n; i++){
        s = (LinkList)malloc(sizeof(LNode));
        s->data = a[i];
        s->next = L->next;
        L->next = s;
    }
    return L;
}
```

### 12.尾插建立链表

```C
LinkList TailCreateList(LinkList &L, int a[], int n){
    L = (LinkList)malloc(sizeof(LNode));
    L->next = NULL;
    LNode *s, *p = L;
    
    for(int i = 0; i < n; i++){
        s = (LinkList)malloc(sizeof(LNode));
        s->data = a[i];
        p->next = s;
        p = s;
    }
    s->next = NULL:
    return L;
}
```

### 13.删除节点

```C
LinkList ListDelet(LinkList L, int i, int *data){
    LNode *p, *q;
    if(i < 0 && i > Length(L)){
        print("error");
        return false;
    }
    p = GetElem(L, i-1);
    q = p->next;
    data = q->data;
    p ->next = q->next;
    free(q);
}
```

### 14.打印节点

```C
void PrintList(LinkList L){
    LNode *p;
    p = L->next;
    int i = 1;
    if(Empty(L)){
        print("Empty!\n");
    }
    while(p != NULL){
        print("LinkList %d' data is %d", i, p->data);
        p = p->next;
        i++;
    }
}
```

### 15.销毁节点

```C
void DestroyList(LinkList &L){
    LNode = *p;
    while(L){
        p = L->next;
        free(L);
        L = p;
    }
}
```

### 16.翻转链表

- 循环 

```C
LinkList ReverseList(LinkList L){
    LNode *pNext, *pPre = NULL;

    if(L == NULL || L->next = L){
        return L;
    }
    while(L != NULL){
        pNext = L->next;
        L->next = pPre;
        pPre = L;
        L = pNext;
    }
    return L;
}
```

- 迭代

```C
LinkList ReverseList(LinkList L){
    if(L == NULL || L->next == NULL){
        return L;
    }
    LNode *NewHead = ReverseList(L->next);
    L->next->next = L;
    L->next = NULL;
    return NewHead;
}
```
  
### 17.不遍历链表删除非尾节点

```C
void RemoveNodeNotTail(LNode *p){
    LNode *pNext = p->next;
    p->dat = pNext->data;
    p->next = pNext->next;
    free(pNext);
}
```

### 18.遍历一次找到中间节点

```C
LNode* Findmid(LinkList L){
    LNode *pSlow = L;
    LNode *pFast = L->next;
    assert(L);
    while(pFast){
        pSlow = pSlow->next;
        pFast = pFast->next->next;
    }
    return pSlow;
}
```

### 19.遍历一遍，找到倒数第k个节点(k从1开始)

```C
LNode* FindK(LinkList L){
    LNode *pSlow = L;
    LNode *pFast = L;
    while(k){
        pFast = pFast->next;
        k--;
    }
    while(pFast){
        pSlow = pSlow->next;
        pFast = pFast->next
    }
    return pSlow;
} 
```

### 20.冒泡排序

```C
LinkList BubbleSort(LinkList L){
    LNode *tail = NULL;
    LNode *Count;
    if(L == NULL || L->next == NULL){
        return;
    }
    /*排序次数*/
    for(Count = L->next; Count != NULL; Count = Count->next){
        LNode *p = L->next;
        for(; p->next != tail; p = p->next){
            if(cmp(p->data, p->next->data)){
                swap(&p->data, &p->next->data)
            }
        }
        tail = p;
    }
    return L;
}

bool cmp(int a, int b){
    return(a>b?1:0); //升序
    /*
    return(a<b?1:0); //降序
    */
}

void swap(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

### 21.插入排序

```C
LinkList InsertSort(LinkList L){
    LNode *p = L->next->next;
    L->next->next = NULL;

    while(p != NULL){
        LNode *p = p->next;
        LNode *pre = L;
        while(pre->next!=NULL && cmp(pre->next->data,p->data){
            pre = pre->next;
        }
        p->next = pre->next;
        pre->next = p;
        p = q;
    }
    return L;
}
```

### 22.快速排序

```C
void QuickSort(LNode *left, LNode *right){
    
    if(left =+ right || left->next == NULL){
        return;
    }
    LNode *pivot_index = Partition(left, right);
    QuickSort(left, pivot_index);
    QuickSort(pivot_index->next, right);

}

LNode* Partition(LNode *left, LNode *right){
    
    LNode *p1 = left;
    LNode *p2 = p1->next;
    int pivot = left->data;
    while(p2 != right){
        if (cmp(p2->data, left->data)){
            swap(p1->next->data, p2->data)
        }
        p2 = p2->next;
    }

}

bool cmp(int a, int b){
    return(a>b?1:0); //升序
    /*
    return(a<b?1:0); //降序
    */
}

void swap(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

### 23.合并两个有序链表

```C
LinkList MergeOrderedList(LinkList L1, LinkList L2){
    LNode *p = NULL;

    while(L1 && L2){
        if(p = NULL){
            if(L1->next->dat <= L2->next->data){
                p = L1;
                L1 = L1.next;
            }else{
                p = L2;
                L2 = L2->next;
            }
        }
        if(p != NULL && (L1->data <= L2->data)){
            p->next = L1;
            L1 = L1->next;
            p = p->next;
        }
        else if(p != NULL && (L1->data > L2->data)){
            p->next = L2;
            L2 = L2->next;
            p = p->next;
        }
    }
    if(L1 == NULL){
        p->next = L2;
    }
    if(L2 == NULL){
        p->next = L1;
    }
    return L;
}
```

### 24.判断链表是否有环，如果有环，求长度和入口

```C
//判断是否有环
int LinkListHasCycle(LNode *head){
    if(head == NULL){
        return head;
    }

    LNode *pslow = head;
    LNode *pfast = head;
    
    while(pfast != NULL && pfast->next->next != NULL){
        pslow = pslow->next;
        pfast = pfast->next->next;
        if(pslow == pfast){
            return 1;
        }
    }
    return 0;
}
//返回相遇节点
LNode* LinkListHasCycle1(LNode *head){
    if(head == NULL){
        return head;
    }

    LNode *pslow = head;
    LNode *pfast = head;
    
    while(pfast != NULL && pfast->next->next != NULL){
        pslow = pslow->next;
        pfast = pfast->next->next;
        if(pslow == pfast){
            return pslow;
        }
    }
    return NULL;
}

//求环的长度
int LinkListGetCycleLen(LNode *head){
    if(head == NULL){
        return NULL;
    }
    LNode *pmeet = LinkListHasCycle1(head);
    if(pmeet == NULL){
        return 0;
    }
    LNode *p = pmeet->next;
    int len = 1;
    while(p != pmeet){
        p = p->next;
        ++len;
    }

    return Len;
}
//环的入口,首元素节点到入口的长度等于相遇点到入口点的长度。
LNode* LinkListGetCycleEnter(LNode *head){
    if(head == NUll){
        return NULL;
    }
    LNode *p1 = head;
    LNode *p2 = LinkListHasCycle1(head);
    while(p1 != p2){
        p1 = p1->next;
        p2 = p2->next;
    }
    return p1;
}
```

## 二：Python实现链表
```Python

class LNode:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_

class LinkList:
    def __init__(self):
        self.__head = None
    
    def Empty(self):
        return self.__head is None
    
    def __len__(self):
        length = 0
        current = self.__head
        while current != None:
            current = current.next
            length += 1
        return length
    
    def HeadInsert(self, elem):
        node = LNode(elem)
        node.next = self.__head
        self.__head = node

    def TailInsert(self, elem):
        node = LNode(elem)
        current = self.__head
        if self.Empty():
            self.__head = None
        else:
            while current.next is not None:
                current = current.next
            current.next = node
    
    def InsertLinkList(self, index, elem):
        if index <= 0 or index > len(slef):
            raise IndexError('error index')
        elif index == 1:
            slef.HeadInsert(elem)
        elif index == len(slef) + 1:
            self.TailInsert(elem)
        else:
            node = LNode(elem)
            curren = slef.__head
            
        





```
如果你喜欢这篇文章,请给我点赞、分享；如果你不喜欢这篇文章，或者发现我的文章错误的地方，请在站内私信我，或者直接给我发邮件(cqcqhelloworld@gmail.com)。
