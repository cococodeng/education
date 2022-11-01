#LaTeX 

**Создать гибкие ссылки в документе**:

`\ref - разместить там, откуда мы на что-то ссылаемся (откуда), \label - разместить там, где лежит то, на что мы ссылаемся (куда)`
```tex
\point Список поддерживаемых драйверов U-Boot приведен в таблице \ref{tab:uboot-drivers}.
\begin{table}[h]
\caption{Драйверы U-Boot}
\label{tab:uboot-drivers}
\centering
\begin{tabular}{|l|p{10cm}|l|}
\hline
Драйвер & Применение & Лицензия \\ \hline \hline
CPU, L1\$, L2\$ & Инициализация CPU. & GPL \\ \hline
GIC & Инициализация GIC, настройка прерываний. & \\ \hline
Ethernet PHY & Загрузка Linux по сети. & GPL \\ \hline
\end{tabular}
\end{table}
```

**Labels Types**

| Label    | Description           |
|----------|-----------------------|
| ch:      | chapter               |
| sec:     | section               |
| subsec:  | subsection            |
| fig:     | figure                |
| tab:     | table                 |
| eq:      | equation              |
| lst:     | code listing          |
| itm:     | enumerated list item  |
| alg:     | algorithm             |
| app:     | appendix subsection   |