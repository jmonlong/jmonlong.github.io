\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cv}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions
\LoadClass{article}
\RequirePackage{ltxtable}
\RequirePackage{ifthen}
\RequirePackage{color}
\RequirePackage[
	pdftex,
	pdfstartview={XYZ 0 1000 1.0},
	bookmarks=false,
	colorlinks,
	breaklinks=true,
	citecolor=black,
	filecolor=black,
	linkcolor=black,
	urlcolor=urlcolor,
	pdfborder={0 0 0}
]{hyperref}
\RequirePackage{geometry}
\RequirePackage{graphicx}

\pagestyle{empty}
\parindent=0pt

\newlength{\colwidth}

\toksdef\ta=0
\toksdef\tb=2
\def\CV@AppendItem#1#2{
	\ta={#1}
	\tb=\expandafter{#2}
	\global\edef#2{\the\tb\the\ta}
}

\newcommand{\CV@init}[1]{
	\expandafter\global\expandafter\def\csname @@#1\endcsname{}
}

\newcommand{\superscript}[1]{\ensuremath{^\textrm{\scriptsize#1}}}
\newcommand{\subscript}[1]{\ensuremath{_\textrm{\scriptsize#1}}}

\newcommand{\xst}[0]{\superscript{st}}
\newcommand{\xnd}[0]{\superscript{nd}}
\newcommand{\xrd}[0]{\superscript{rd}}
\newcommand{\xth}[0]{\superscript{th}}

\def\detailedOnly{0}
\def\@@language{}
\def\@@detailed{}

\newcommand{\Language}[1]{
	\global\def\@@language{#1}
}

\newcommand{\Detailed}[1]{
	\global\def\@@detailed{#1}
}

\newlength{\scolwidth}
\newlength{\mcolwidth}
\newlength{\cmedskip}
\newlength{\sbigskip}
\newlength{\smedskip}
\newlength{\ssmallskip}

\newcommand{\CV@initLength}{
	\setlength{\scolwidth}{\textwidth}
	\addtolength{\scolwidth}{-\colwidth}
	\addtolength{\scolwidth}{-8.72mm}		% Je ne comprends pas d'où vient cette dimension, mais ça marche bien...

	\setlength{\mcolwidth}{\colwidth}
	\addtolength{\mcolwidth}{\scolwidth}
	\addtolength{\mcolwidth}{4.36mm}		% Idem (si ce n'est que c'est la moitié de la première)

	\setlength{\cmedskip}{\medskipamount}
	\addtolength{\cmedskip}{-\smallskipamount}
	\addtolength{\cmedskip}{-\baselineskip}

	\setlength{\sbigskip}{\bigskipamount}
	\addtolength{\sbigskip}{-\baselineskip}
	\setlength{\smedskip}{\medskipamount}
	\addtolength{\smedskip}{-\baselineskip}
	\setlength{\ssmallskip}{\smallskipamount}
	\addtolength{\ssmallskip}{-\baselineskip}
}

\def\@@name{}
\def\@@address{}
\def\@@telephone{}
\def\@@email{}
\def\@@nationality{}
\def\@@dateofbirth{}
\def\@@age{}
\def\@@gender{}
\def\@@maritalstatus{}
\def\@@drivinglicense{}
\def\@@webpage{}

\newenvironment{heading}{
	\CV@init{name}
	\CV@init{address}	
	\CV@init{telephone}
	\CV@init{email}
	\CV@init{nationality}
	\CV@init{dateofbirth}
	\CV@init{age}
	\CV@init{gender}
	\CV@init{maritalstatus}
	\CV@init{mobility}
	\CV@init{photo}
	\CV@init{webpage}
	\newcommand{\Name}[1]{\global\def\@@name{##1}}
	\newcommand{\Address}[1]{\global\def\@@address{##1}}	
	\newcommand{\Telephone}[1]{\global\def\@@telephone{##1}}
	\newcommand{\Email}[1]{\global\def\@@email{##1}}
	\newcommand{\Nationality}[1]{\global\def\@@nationality{##1}}
	\newcommand{\DateOfBirth}[1]{\global\def\@@dateofbirth{##1}}
	\newcommand{\Age}[1]{\global\def\@@age{##1}}
	\newcommand{\Gender}[1]{\global\def\@@gender{##1}}
	\newcommand{\MaritalStatus}[1]{\global\def\@@maritalstatus{##1}}
	\newcommand{\Mobility}[1]{\global\def\@@mobility{##1}}
	\newcommand{\Photo}[1]{\global\def\@@photo{##1}}
	\newcommand{\Webpage}[1]{\global\def\@@webpage{##1}}
}{
	\global\def\CV@delayed{}

	\CV@AppendItem{
		\hspace*{\tabcolsep}
		\begin{minipage}[c]{0.5\linewidth}
		\vspace{-\baselineskip}		% Mais pourquoi ?
                \scriptsize
	}{\CV@delayed}

	\ifx\@@name\empty\else
		\CV@AppendItem{{\large \@@name}\newline}{\CV@delayed}
	\fi

	\ifx\@@dateofbirth\empty\else
		\ifthenelse{\equal{\@@language}{francais}}{
			\ifthenelse{\equal{\@@gender}{M}}{
				\CV@AppendItem{Né le }{\CV@delayed}
			}{
				\CV@AppendItem{Née le }{\CV@delayed}
			}
			\CV@AppendItem{\@@dateofbirth}{\CV@delayed}
			\ifx\@@age\empty\else
				\CV@AppendItem{ (\@@age{} ans)}{\CV@delayed}
			\fi
		}{}
		\ifthenelse{\equal{\@@language}{english}}{
			\CV@AppendItem{Date of birth: \@@dateofbirth}{\CV@delayed}
			\ifx\@@age\empty\else
				\CV@AppendItem{ (\@@age{} year old)}{\CV@delayed}
			\fi
		}{}
		\ifthenelse{\equal{\@@language}{espanol}}{
			\CV@AppendItem{Fecha de nacimiento: \@@dateofbirth}{\CV@delayed}
			\ifx\@@age\empty\else
				\CV@AppendItem{ (\@@age{} year old)}{\CV@delayed}
			\fi
		}{}
	\fi

	\ifx\@@nationality\empty\else
		\ifthenelse{\equal{\@@language}{francais}}{
			\CV@AppendItem{\newline{}Nationalité \@@nationality}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{english}}{
			\CV@AppendItem{\newline{}Nationality: \@@nationality}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{espanol}}{
			\CV@AppendItem{\newline{}Nacionalidad: \@@nationality}{\CV@delayed}
		}{}
	\fi

	\ifx\@@address\empty\else
		\CV@AppendItem{\@@address\newline}{\CV@delayed}
	\fi

	\ifx\@@telephone\empty\else
		\ifthenelse{\equal{\@@language}{francais}}{
			\CV@AppendItem{Tél.~: \@@telephone\newline}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{english}}{
			\CV@AppendItem{Phone: \@@telephone\newline}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{espanol}}{
			\CV@AppendItem{Tel: \@@telephone\newline}{\CV@delayed}
		}{}
	\fi

	\ifx\@@email\empty\else
		\ifthenelse{\equal{\@@language}{francais}}{
			\CV@AppendItem{Email~: \href{mailto:\@@email}{\@@email}\newline}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{english}}{
			\CV@AppendItem{Email: \href{mailto:\@@email}{\@@email}\newline}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{espanol}}{
			\CV@AppendItem{Email: \href{mailto:\@@email}{\@@email}\newline}{\CV@delayed}
		}{}
	\fi

	\ifx\@@webpage\empty\else
		\ifthenelse{\equal{\@@language}{francais}}{
			\CV@AppendItem{Page en ligne~: \href{\@@webpage}{\@@webpage}}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{english}}{
			\CV@AppendItem{Webpage: \href{\@@webpage}{\@@webpage}}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{espanol}}{
			\CV@AppendItem{Webpage: \href{\@@webpage}{\@@webpage}}{\CV@delayed}
		}{}
	\fi

	\ifx\@@mobility\empty\else
		\CV@AppendItem{\newline{}\@@mobility}{\CV@delayed}
	\fi


	\CV@AppendItem{
		\end{minipage}
		\begin{minipage}[c]{0.3\linewidth}
                  % \vspace{\baselineskip}
                  \normalsize
	}{\CV@delayed}

	\ifx\@@maritalstatus\empty\else
		\ifthenelse{\equal{\@@language}{francais}}{
			\CV@AppendItem{\newline{}\@@maritalstatus}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{english}}{
			\CV@AppendItem{\newline{}Marital status: \@@maritalstatus}{\CV@delayed}
		}{}
		\ifthenelse{\equal{\@@language}{espanol}}{
			\CV@AppendItem{\newline{}\@@maritalstatus}{\CV@delayed}
		}{}
	\fi

	\ifx\@@photo\empty\else
        \CV@AppendItem{
        \end{minipage}
        \hfill
        \begin{minipage}[c]{0.17\linewidth}
          \flushright
          \vspace{-\baselineskip}
          \includegraphics[height=2.5cm]{\@@photo}
        }{\CV@delayed}
	\fi

	\CV@AppendItem{
		\end{minipage}
		\vspace{-\baselineskip}
		\bigskip
	}{\CV@delayed}

	\aftergroup\CV@delayed
}

\newenvironment{objective}{
	\CV@initLength

	\begin{longtable}{p{\colwidth}p{\scolwidth}}

	\ifthenelse{\equal{\@@language}{francais}}{
		\large\itshape Objectif~: & \large\itshape
	}{}\ignorespaces
	\ifthenelse{\equal{\@@language}{english}}{
		\large\itshape Objective: & \large\itshape
	}{}\ignorespaces
	\ifthenelse{\equal{\@@language}{espanol}}{
		\large\itshape Objetivo: & \large\itshape
	}{}\ignorespaces
}{
	\\
	\end{longtable}
	\medskip
}

\renewenvironment{section}[1]{
	\CV@initLength

	\vspace{\cmedskip}
	\textbf{\large #1}\par
	\rule[3mm]{\textwidth}{0.1mm}\par
	\vspace{-4mm}
	\begin{longtable}{p{\colwidth}p{\scolwidth}}
%	\tabularx{\linewidth}{p{\colwidth}X}
}{
%	\endtabularx
	\end{longtable}
}

\def\@@date{}
\def\@@duration{}
\def\@@place{}
\def\@@locality{}
\def\@@country{}
\def\@@activities{}
\def\@@events{}

\newcommand{\CV@add@activity}[2][1]{
	\ifthenelse{\equal{\@@detailed}{1} \or \equal{#1}{1}}{
		\ifx\@@activities\empty\else
			\CV@AppendItem{\newline}{\@@activities}
		\fi
	
		\CV@AppendItem{#2.}{\@@activities}
	}{}
}

\newcommand{\CV@add@event}[2][1]{
	\ifthenelse{\equal{\@@detailed}{1} \or \equal{#1}{1}}{
		\ifx\@@events\empty\else
			\CV@AppendItem{\newline}{\@@events}
		\fi
	
		\CV@AppendItem{#2.}{\@@events}
	}{}
}

\newcommand{\CV@add@course}[1]{
	\ifthenelse{\equal{\@@detailed}{1}}{
		\CV@AppendItem{\ensuremath{\triangleright}~#1. }{\@@courses}
	}{}
}

\newcommand{\singleEntry}[2][1]{
	\ifthenelse{\equal{\@@detailed}{1} \or \equal{#1}{1}}{
		\\\kill
		\multicolumn{2}{p{\mcolwidth}}{#2.}\\
	}{}
%	\\[\ssmallskip]
}

\newcommand{\bigSkip}{
	\\[\sbigskip]
}

\newcommand{\medSkip}{
	\\[\smedskip]
}

\newcommand{\smallSkip}{
	\\[\ssmallskip]
}

\newenvironment{entry}[1][1]{
	\global\def\@@detail{#1}

	\CV@init{date}
	\CV@init{duration}
	\CV@init{skill}
	\CV@init{place}
	\CV@init{locality}
	\CV@init{country}
	\CV@init{activities}
	\CV@init{events}
	\CV@init{courses}
	\newcommand{\Date}[1]{\global\def\@@date{##1}}
	\newcommand{\Duration}[1]{\global\def\@@duration{##1}}
	\newcommand{\Skill}[1]{\global\def\@@skill{##1}}
	\newcommand{\Place}[1]{\global\def\@@place{##1}}
	\newcommand{\Locality}[1]{\global\def\@@locality{##1}}
	\newcommand{\Country}[1]{\global\def\@@country{##1}}
	\let\Activity\CV@add@activity
	\let\Event\CV@add@event
	\let\Course\CV@add@course
}{
	\global\def\CV@delayed{}	
	\CV@AppendItem{\\\kill}{\CV@delayed}

	\ifthenelse{\equal{\@@detailed}{1} \or \equal{\@@detail}{1}}{
		\ifx\@@date\empty\else
			\CV@AppendItem{\textbf{\@@date}}{\CV@delayed}
			\ifx\@@duration\empty\else
				\CV@AppendItem{\newline}{\CV@delayed}
			\fi
		\fi
	
		\ifx\@@duration\empty\else
			\CV@AppendItem{(\@@duration)}{\CV@delayed}
		\fi
	
		\ifx\@@skill\empty\else
			\CV@AppendItem{\@@skill}{\CV@delayed}
		\fi
	
		\CV@AppendItem{&}{\CV@delayed}
	
		\ifx\@@place\empty\else
			\CV@AppendItem{\textsc{\@@place}}{\CV@delayed}
			\ifx\@@locality\empty\else
				\CV@AppendItem{, \@@locality}{\CV@delayed}
			\fi
			\ifx\@@country\empty\else
				\CV@AppendItem{, \@@country}{\CV@delayed}
			\fi
			\CV@AppendItem{.}{\CV@delayed}
	
			\ifthenelse{\equal{\@@activities}{\empty} \and \equal{\@@events}{\empty} \and \equal{\@@courses}{\empty}}{}{
				\CV@AppendItem{\newline}{\CV@delayed}
			}	
		\fi
	
		\ifx\@@activities\empty\else
			\CV@AppendItem{\@@activities}{\CV@delayed}
	
			\ifthenelse{\equal{\@@events}{\empty} \and \equal{\@@courses}{\empty}}{}{
				\CV@AppendItem{\newline}{\CV@delayed}
			}	
		\fi
	
		\ifx\@@events\empty\else
			\CV@AppendItem{\@@events}{\CV@delayed}
	
			\ifthenelse{\equal{\@@courses}{\empty}}{}{
				\CV@AppendItem{\newline}{\CV@delayed}
			}	
		\fi
	
		\ifx\@@courses\empty\else
			\CV@AppendItem{\textit{\@@courses}}{\CV@delayed}
		\fi
	
		\CV@AppendItem{\\[\smallskipamount]}{\CV@delayed}
	}{}

	\aftergroup\CV@delayed
}
