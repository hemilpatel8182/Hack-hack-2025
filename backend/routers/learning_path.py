from fastapi import APIRouter, Depends, HTTPException, Body
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from models import LearningPath

router = APIRouter(
    prefix="/learning_path",
    tags=["Learning Path"]
)

class PathRequest(BaseModel):
    user_goal: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🎯 Prebuilt learning paths
prebuilt_paths = {
    "Budgeting Basics": [
        {
            "step": 1,
            "title": "Why Budgeting Matters",
            "description": "Learn why budgeting is critical.",
            "chapters": [
                {"chapter": 1, "title": "Intro to Budgeting"},
                {"chapter": 2, "title": "Common Mistakes"}
            ],
            "resources": [
                {"type": "video", "title": "Why Budgeting is Important", "link": "https://www.youtube.com/watch?v=GqQQhJX5G1I"},
                {"type": "article", "title": "Budgeting Basics Guide", "link": "https://www.investopedia.com/terms/b/budget.asp"}
            ],
            "quizzes": [
                {
                    "chapter": 1,
                    "questions": [
                        {
                            "question": "Why is budgeting important?",
                            "options": ["To spend more freely", "To control where your money goes", "To get more credit cards", "To ignore financial planning"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "Budgeting can help you avoid...",
                            "options": ["Saving money", "Debt and overspending", "Earning more", "Working extra jobs"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "Which is a benefit of having a budget?",
                            "options": ["Unlimited shopping", "Organized finances", "Higher taxes", "More debt"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "People who don't budget often...",
                            "options": ["Save too much", "Lose track of expenses", "Have perfect credit scores", "Invest wisely"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "Budgeting mainly encourages...",
                            "options": ["Spending all earnings", "Ignoring bills", "Conscious money management", "Gambling investments"],
                            "correctAnswer": 2
                        }
                    ]
                }
            ]
        },
        {
            "step": 2,
            "title": "Setting Financial Goals",
            "description": "How to set achievable financial goals.",
            "chapters": [
                {"chapter": 1, "title": "Short vs Long Term Goals"},
                {"chapter": 2, "title": "Tracking Progress"}
            ],
            "resources": [
                {"type": "video", "title": "How to Set Financial Goals", "link": "https://www.youtube.com/watch?v=CbyJq3N-JmE"},
                {"type": "article", "title": "Nerdwallet Guide: Set Financial Goals", "link": "https://www.nerdwallet.com/article/finance/set-financial-goals"}
            ],
            "quizzes": [
                {
                    "chapter": 2,
                    "questions": [
                        {
                            "question": "What are financial goals?",
                            "options": ["Random shopping lists", "Specific money targets", "Imaginary numbers", "Spending limits only"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "Short-term financial goals usually take...",
                            "options": ["Less than a year", "5–10 years", "20 years", "A lifetime"],
                            "correctAnswer": 0
                        },
                        {
                            "question": "Tracking your financial goals helps you...",
                            "options": ["Spend without thinking", "Stay motivated and adjust plans", "Forget your budget", "Always borrow money"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "Which of these is a long-term financial goal?",
                            "options": ["Buying groceries", "Paying rent", "Saving for retirement", "Paying a small utility bill"],
                            "correctAnswer": 2
                        },
                        {
                            "question": "Setting unrealistic financial goals can lead to...",
                            "options": ["More success", "Faster savings", "Frustration and giving up", "Higher income"],
                            "correctAnswer": 2
                        }
                    ]
                }
            ]
        },
        {
            "step": 3,
            "title": "Building a Simple Budget",
            "description": "Step-by-step guide to making your first budget.",
            "chapters": [
                {"chapter": 1, "title": "50/30/20 Rule"},
                {"chapter": 2, "title": "Income vs Expenses"}
            ],
            "resources": [
                {"type": "article", "title": "Simple Budgeting Strategies", "link": "https://www.daveramsey.com/blog/the-truth-about-budgeting"},
                {"type": "video", "title": "How to Budget", "link": "https://www.youtube.com/watch?v=ggUdu_VtH3A"}
            ],
            "quizzes": [
                {
                    "chapter": 3,
                    "questions": [
                        {
                            "question": "The 50/30/20 rule suggests you spend 50% on...",
                            "options": ["Wants", "Needs", "Savings", "Investments"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "What is considered a 'need' in budgeting?",
                            "options": ["Netflix subscription", "Dining out", "Rent or mortgage", "Luxury shopping"],
                            "correctAnswer": 2
                        },
                        {
                            "question": "Which is an example of a 'want'?",
                            "options": ["Utility bill", "Car insurance", "Designer clothes", "Grocery shopping"],
                            "correctAnswer": 2
                        },
                        {
                            "question": "To build a budget, you must first know your...",
                            "options": ["Favorite stores", "Total income and expenses", "Preferred payment methods", "Social media followers"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "Saving money should ideally fall under which part of the 50/30/20 rule?",
                            "options": ["50%", "30%", "20%", "70%"],
                            "correctAnswer": 2
                        }
                    ]
                }
            ]
        },
        {
            "step": 4,
            "title": "Sticking to Your Budget",
            "description": "How to actually follow your plan.",
            "chapters": [
                {"chapter": 1, "title": "Discipline Techniques"},
                {"chapter": 2, "title": "Accountability Tips"}
            ],
            "resources": [
                {"type": "article", "title": "Tips for Sticking to a Budget", "link": "https://www.thebalancemoney.com/how-to-stick-to-a-budget-2386033"},
                {"type": "video", "title": "Sticking to Your Budget", "link": "https://www.youtube.com/watch?v=6AdXa_XmwXg"}
            ],
            "quizzes": [
                {
                    "chapter": 4,
                    "questions": [
                        {
                            "question": "What is a common reason people fail to stick to budgets?",
                            "options": ["Strict tracking", "Forgetting to monitor spending", "Saving too much", "Having no wants"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "An accountability partner can help by...",
                            "options": ["Spending your money", "Ignoring your goals", "Encouraging you to stay on track", "Taking over your finances"],
                            "correctAnswer": 2
                        },
                        {
                            "question": "Which technique helps in staying disciplined with budgeting?",
                            "options": ["Daily expense tracking", "Avoiding looking at your bank balance", "Buying impulsively", "Ignoring financial plans"],
                            "correctAnswer": 0
                        },
                        {
                            "question": "Reviewing your budget weekly can help you...",
                            "options": ["Forget bills", "Catch mistakes early", "Spend faster", "Avoid all savings"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "If you overspend in one category, you should...",
                            "options": ["Quit budgeting", "Adjust spending elsewhere", "Ignore it", "Spend even more"],
                            "correctAnswer": 1
                        }
                    ]
                }
            ]
        },
        {
            "step": 5,
            "title": "Reviewing and Adjusting",
            "description": "How to improve your budget over time.",
            "chapters": [
                {"chapter": 1, "title": "Monthly Review"},
                {"chapter": 2, "title": "Adjusting for Big Changes"}
            ],
            "resources": [
                {"type": "article", "title": "Adjusting Your Budget", "link": "https://www.investopedia.com/terms/b/budget.asp"},
                {"type": "video", "title": "When to Update Your Budget", "link": "https://www.youtube.com/watch?v=zNmY7Db5y6Q"}
            ],
            "quizzes": [
                {
                    "chapter": 5,
                    "questions": [
                        {
                            "question": "Why should you review your budget monthly?",
                            "options": ["To find sales", "To adjust for any life changes", "To ignore old goals", "To spend leftover money"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "A life event like a new job should cause you to...",
                            "options": ["Ignore your old budget", "Review and update your budget", "Double your spending", "Stop saving"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "Which is a reason you might adjust your budget?",
                            "options": ["Income increase", "Expense reduction", "Unexpected medical bills", "All of the above"],
                            "correctAnswer": 3
                        },
                        {
                            "question": "What should you do if you consistently underspend?",
                            "options": ["Spend more impulsively", "Increase your savings goals", "Stop tracking expenses", "Ignore extra money"],
                            "correctAnswer": 1
                        },
                        {
                            "question": "The goal of adjusting your budget is to...",
                            "options": ["Make budgeting harder", "Keep your financial plan realistic", "Hide mistakes", "Spend your savings"],
                            "correctAnswer": 1
                        }
                    ]
                }
            ]
        }
    ],

    "How Taxes Work": [
    {
        "step": 1,
        "title": "Understanding Taxes",
        "description": "Learn why taxes exist and how they work.",
        "chapters": [
            {"chapter": 1, "title": "What Are Taxes"},
            {"chapter": 2, "title": "Types of Taxes"}
        ],
        "resources": [
            {"type": "video", "title": "What Are Taxes?", "link": "https://www.youtube.com/watch?v=qKpxd8hzOcQ"},
            {"type": "article", "title": "Investopedia: Taxes Explained", "link": "https://www.investopedia.com/terms/t/tax.asp"}
        ],
        "quizzes": [
            {
                "chapter": 1,
                "questions": [
                    {
                        "question": "Taxes are mainly collected to...",
                        "options": ["Support government services", "Buy luxury cars for officials", "Fund personal vacations", "Increase the national debt"],
                        "correctAnswer": 0
                    },
                    {
                        "question": "Which is an example of a government service funded by taxes?",
                        "options": ["Private gyms", "Police and fire departments", "Online shopping websites", "Fast food chains"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Sales tax is usually applied to...",
                        "options": ["Investment income", "Inheritance", "Purchases at stores", "Bank savings"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Property tax is primarily paid on...",
                        "options": ["Cars", "Houses and land", "Vacation trips", "Jewelry"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Which type of tax directly reduces your paycheck?",
                        "options": ["Sales tax", "Income tax", "Excise tax", "Gift tax"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 2,
        "title": "Income Tax Basics",
        "description": "Understand how income taxes are calculated.",
        "chapters": [
            {"chapter": 1, "title": "Tax Brackets"},
            {"chapter": 2, "title": "Filing Status"}
        ],
        "resources": [
            {"type": "video", "title": "How Income Taxes Work", "link": "https://www.youtube.com/watch?v=2YFdOo8KqgQ"},
            {"type": "article", "title": "IRS Tax Withholding Estimator", "link": "https://www.irs.gov/individuals/tax-withholding-estimator"}
        ],
        "quizzes": [
            {
                "chapter": 2,
                "questions": [
                    {
                        "question": "A tax bracket determines...",
                        "options": ["Your social status", "How much you owe in income taxes", "How much money you spend", "Your retirement plan"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Filing status affects your...",
                        "options": ["Favorite color", "Tax rate and deductions", "Grocery budget", "Vacation plans"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Which filing status typically pays the lowest taxes?",
                        "options": ["Single", "Married Filing Jointly", "Head of Household", "Married Filing Separately"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Income taxes are usually taken out of your paycheck through...",
                        "options": ["Credit cards", "Direct withdrawal", "Payroll withholding", "Personal checks"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Higher income levels are taxed at...",
                        "options": ["Lower rates", "Same flat rates", "Higher rates", "Zero rates"],
                        "correctAnswer": 2
                    }
                ]
            }
        ]
    },
    {
        "step": 3,
        "title": "How to File Taxes",
        "description": "Basics of filing your first tax return.",
        "chapters": [
            {"chapter": 1, "title": "Required Forms"},
            {"chapter": 2, "title": "Common Mistakes"}
        ],
        "resources": [
            {"type": "video", "title": "How to File Your Taxes", "link": "https://www.youtube.com/watch?v=y7SM5xGybZ0"},
            {"type": "article", "title": "Filing Basics by IRS", "link": "https://www.irs.gov/filing"}
        ],
        "quizzes": [
            {
                "chapter": 3,
                "questions": [
                    {
                        "question": "Which form is most commonly used to file personal income taxes in the U.S.?",
                        "options": ["W-2", "1040", "1099", "401(k)"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A W-2 form shows...",
                        "options": ["Your bank balance", "Your total earnings and taxes withheld", "Your investments", "Your insurance plan"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "When filing taxes, it is important to avoid...",
                        "options": ["Keeping receipts", "Double-checking information", "Common mistakes like typos and missing forms", "Filing early"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "If you miss the tax filing deadline without an extension, you might face...",
                        "options": ["Lottery winnings", "Late fees and penalties", "Higher wages", "Free gifts"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "One common way to file taxes online is through...",
                        "options": ["IRS Free File", "A random blog", "Text message", "A public library computer without security"],
                        "correctAnswer": 0
                    }
                ]
            }
        ]
    },
    {
        "step": 4,
        "title": "Deductions and Credits",
        "description": "Lower your tax bill legally using deductions and credits.",
        "chapters": [
            {"chapter": 1, "title": "Standard vs Itemized Deductions"},
            {"chapter": 2, "title": "Common Tax Credits"}
        ],
        "resources": [
            {"type": "video", "title": "Understanding Deductions", "link": "https://www.youtube.com/watch?v=b1_zscZdzOA"},
            {"type": "article", "title": "IRS Credits and Deductions", "link": "https://www.irs.gov/credits-deductions"}
        ],
        "quizzes": [
            {
                "chapter": 4,
                "questions": [
                    {
                        "question": "What is a tax deduction?",
                        "options": ["A fine you pay", "An amount that reduces taxable income", "A tax increase", "A reward program"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Which is a common standard deduction category?",
                        "options": ["Business expenses", "Educational expenses", "Mortgage interest", "Regular living expenses"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "A tax credit directly reduces...",
                        "options": ["Your taxable income", "Your total tax owed", "Your grocery bill", "Your rent"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "The Child Tax Credit is an example of...",
                        "options": ["Deduction", "Tax credit", "Loan", "Tax penalty"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Choosing between standard and itemized deductions depends on...",
                        "options": ["How much you can deduct", "Your favorite color", "Your neighbor’s choice", "Which state you live in"],
                        "correctAnswer": 0
                    }
                ]
            }
        ]
    },
    {
        "step": 5,
        "title": "Planning Ahead for Taxes",
        "description": "Tips for managing taxes throughout the year.",
        "chapters": [
            {"chapter": 1, "title": "Saving Receipts"},
            {"chapter": 2, "title": "Adjusting Withholding"}
        ],
        "resources": [
            {"type": "article", "title": "Smart Tax Planning", "link": "https://www.investopedia.com/articles/pf/07/year_end_tax_tips.asp"},
            {"type": "video", "title": "Tax Planning Basics", "link": "https://www.youtube.com/watch?v=fWbIftJKLRk"}
        ],
        "quizzes": [
            {
                "chapter": 5,
                "questions": [
                    {
                        "question": "Saving receipts during the year helps with...",
                        "options": ["Decorating", "Proving deductions", "Buying more items", "Filing for bankruptcy"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Adjusting your withholding means...",
                        "options": ["Changing your grocery list", "Updating how much tax is taken from your paycheck", "Shopping for gadgets", "Forgetting about taxes"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "If you expect to owe a lot at tax time, you should...",
                        "options": ["Ignore it", "Adjust your payroll withholding", "Buy expensive items", "Skip tax filing"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Making estimated tax payments is important for...",
                        "options": ["Employees only", "Self-employed workers", "Retirees", "Teenagers"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Planning ahead for taxes can help you avoid...",
                        "options": ["Big surprise tax bills", "Grocery shopping", "Extra vacation days", "Over-saving money"],
                        "correctAnswer": 0
                    }
                ]
            }
        ]
    }
],

    "Understanding Credit Score": [
    {
        "step": 1,
        "title": "What is a Credit Score?",
        "description": "Understand the basics of credit scores.",
        "chapters": [
            {"chapter": 1, "title": "FICO vs VantageScore"},
            {"chapter": 2, "title": "Credit Score Ranges"}
        ],
        "resources": [
            {"type": "video", "title": "Credit Score Explained", "link": "https://www.youtube.com/watch?v=3B9bS2NWHq8"},
            {"type": "article", "title": "Credit Score Basics - NerdWallet", "link": "https://www.nerdwallet.com/article/finance/credit-score-basics"}
        ],
        "quizzes": [
            {
                "chapter": 1,
                "questions": [
                    {
                        "question": "A credit score mainly shows...",
                        "options": ["Your total savings", "Your borrowing reliability", "Your school grades", "Your salary"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Which two models are most common for credit scores?",
                        "options": ["IRS and DMV", "FICO and VantageScore", "Apple and Samsung", "FHA and VA"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A typical credit score range is between...",
                        "options": ["100–400", "300–850", "500–1200", "0–100"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A higher credit score usually means...",
                        "options": ["Higher loan interest", "Lower creditworthiness", "Better chances of loan approval", "Worse credit options"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "A poor credit score can result in...",
                        "options": ["Lower loan rates", "Denied loan applications", "Increased salary", "Free vacations"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 2,
        "title": "How Scores Are Calculated",
        "description": "Learn what affects your credit score.",
        "chapters": [
            {"chapter": 1, "title": "Payment History"},
            {"chapter": 2, "title": "Credit Utilization"}
        ],
        "resources": [
            {"type": "video", "title": "How Credit Scores Work", "link": "https://www.youtube.com/watch?v=_HjExXkx3_w"},
            {"type": "article", "title": "Factors Impacting Your Score", "link": "https://www.experian.com/blogs/news/2019/05/five-factors-affect-credit-scores/"}
        ],
        "quizzes": [
            {
                "chapter": 2,
                "questions": [
                    {
                        "question": "The biggest factor affecting credit scores is...",
                        "options": ["Credit utilization", "New credit", "Payment history", "Types of credit"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Credit utilization refers to...",
                        "options": ["Your total income", "How much of your available credit you use", "Your job usage", "Investment returns"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Paying bills late can...",
                        "options": ["Improve your credit", "Lower your credit score", "Double your credit limit", "Remove your debt"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A good credit utilization rate is usually...",
                        "options": ["Above 90%", "Between 50%–70%", "Below 30%", "Exactly 100%"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Opening too many new accounts at once can...",
                        "options": ["Boost your score instantly", "Lower your score temporarily", "Cancel old debts", "Increase your salary"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 3,
        "title": "Building Credit",
        "description": "Ways to build a strong credit history.",
        "chapters": [
            {"chapter": 1, "title": "Using Credit Responsibly"},
            {"chapter": 2, "title": "Secured Cards"}
        ],
        "resources": [
            {"type": "video", "title": "Building Credit From Scratch", "link": "https://www.youtube.com/watch?v=umQeGJKhGY8"},
            {"type": "article", "title": "How to Build Credit Fast", "link": "https://www.nerdwallet.com/article/finance/how-to-build-credit"}
        ],
        "quizzes": [
            {
                "chapter": 3,
                "questions": [
                    {
                        "question": "One way to build credit is by...",
                        "options": ["Not using any credit at all", "Using a secured credit card", "Taking multiple payday loans", "Paying cash only"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Paying your credit card balance in full each month...",
                        "options": ["Hurts your score", "Has no effect", "Helps your credit score", "Triggers extra fees"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "A secured card requires...",
                        "options": ["A co-signer", "A deposit as collateral", "No payments ever", "A high credit score already"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Keeping old credit accounts open...",
                        "options": ["Lowers your score", "Has no impact", "Lengthens your credit history positively", "Deletes credit history"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Credit-building loans are mostly offered by...",
                        "options": ["Gyms", "Banks and credit unions", "Grocery stores", "Airlines"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 4,
        "title": "Fixing Bad Credit",
        "description": "Recover from a poor credit history.",
        "chapters": [
            {"chapter": 1, "title": "Debt Repayment"},
            {"chapter": 2, "title": "Disputing Errors"}
        ],
        "resources": [
            {"type": "article", "title": "How to Fix Bad Credit", "link": "https://www.experian.com/blogs/news/2019/06/improve-credit-score/"},
            {"type": "video", "title": "Fixing Your Credit Score", "link": "https://www.youtube.com/watch?v=ETdEJSRCE1I"}
        ],
        "quizzes": [
            {
                "chapter": 4,
                "questions": [
                    {
                        "question": "To fix bad credit, start by...",
                        "options": ["Ignoring debt collectors", "Repaying debts on time", "Closing all accounts", "Filing for bankruptcy immediately"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Disputing errors on your credit report can...",
                        "options": ["Hurt your score", "Improve your score if errors are removed", "Freeze your credit forever", "Make loans free"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Paying off collections can...",
                        "options": ["Instantly remove them", "Slowly help improve your score", "Hurt your score more", "Cancel your taxes"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Regularly checking your credit report can help catch...",
                        "options": ["Identity theft", "New TV shows", "Traffic violations", "Grocery discounts"],
                        "correctAnswer": 0
                    },
                    {
                        "question": "Debt repayment plans can be created with help from...",
                        "options": ["Friends only", "Certified credit counselors", "Gas station attendants", "Gamers"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 5,
        "title": "Maintaining Good Credit",
        "description": "Keeping your credit strong over time.",
        "chapters": [
            {"chapter": 1, "title": "Monitoring Reports"},
            {"chapter": 2, "title": "Preventing Fraud"}
        ],
        "resources": [
            {"type": "video", "title": "Credit Monitoring Tips", "link": "https://www.youtube.com/watch?v=gQf9c_oW5tw"},
            {"type": "article", "title": "Protect Your Credit", "link": "https://www.consumer.ftc.gov/articles/how-keep-your-personal-information-secure"}
        ],
        "quizzes": [
            {
                "chapter": 5,
                "questions": [
                    {
                        "question": "Monitoring your credit reports helps you...",
                        "options": ["Decrease your income", "Spot errors early", "Get more junk mail", "Lower your phone bill"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Fraud prevention is important because...",
                        "options": ["Fraud boosts your credit", "Identity theft can harm your credit score", "It makes shopping faster", "It reduces your taxes"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Using two-factor authentication protects your...",
                        "options": ["Travel plans", "Credit accounts", "Cooking recipes", "Fitness routines"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "You should check your credit reports at least...",
                        "options": ["Once every 10 years", "Never", "Once a year", "Every week"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Setting up alerts with banks can help detect...",
                        "options": ["New shopping deals", "Unauthorized transactions", "New movies", "Lottery winnings"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    }
    ],

    "Understanding Credit Score": [
    {
        "step": 1,
        "title": "What is a Credit Score?",
        "description": "Understand the basics of credit scores.",
        "chapters": [
            {"chapter": 1, "title": "FICO vs VantageScore"},
            {"chapter": 2, "title": "Credit Score Ranges"}
        ],
        "resources": [
            {"type": "video", "title": "Credit Score Explained", "link": "https://www.youtube.com/watch?v=3B9bS2NWHq8"},
            {"type": "article", "title": "Credit Score Basics - NerdWallet", "link": "https://www.nerdwallet.com/article/finance/credit-score-basics"}
        ],
        "quizzes": [
            {
                "chapter": 1,
                "questions": [
                    {
                        "question": "A credit score mainly shows...",
                        "options": ["Your total savings", "Your borrowing reliability", "Your school grades", "Your salary"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Which two models are most common for credit scores?",
                        "options": ["IRS and DMV", "FICO and VantageScore", "Apple and Samsung", "FHA and VA"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A typical credit score range is between...",
                        "options": ["100–400", "300–850", "500–1200", "0–100"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A higher credit score usually means...",
                        "options": ["Higher loan interest", "Lower creditworthiness", "Better chances of loan approval", "Worse credit options"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "A poor credit score can result in...",
                        "options": ["Lower loan rates", "Denied loan applications", "Increased salary", "Free vacations"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 2,
        "title": "How Scores Are Calculated",
        "description": "Learn what affects your credit score.",
        "chapters": [
            {"chapter": 1, "title": "Payment History"},
            {"chapter": 2, "title": "Credit Utilization"}
        ],
        "resources": [
            {"type": "video", "title": "How Credit Scores Work", "link": "https://www.youtube.com/watch?v=_HjExXkx3_w"},
            {"type": "article", "title": "Factors Impacting Your Score", "link": "https://www.experian.com/blogs/news/2019/05/five-factors-affect-credit-scores/"}
        ],
        "quizzes": [
            {
                "chapter": 2,
                "questions": [
                    {
                        "question": "The biggest factor affecting credit scores is...",
                        "options": ["Credit utilization", "New credit", "Payment history", "Types of credit"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Credit utilization refers to...",
                        "options": ["Your total income", "How much of your available credit you use", "Your job usage", "Investment returns"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Paying bills late can...",
                        "options": ["Improve your credit", "Lower your credit score", "Double your credit limit", "Remove your debt"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A good credit utilization rate is usually...",
                        "options": ["Above 90%", "Between 50%–70%", "Below 30%", "Exactly 100%"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Opening too many new accounts at once can...",
                        "options": ["Boost your score instantly", "Lower your score temporarily", "Cancel old debts", "Increase your salary"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 3,
        "title": "Building Credit",
        "description": "Ways to build a strong credit history.",
        "chapters": [
            {"chapter": 1, "title": "Using Credit Responsibly"},
            {"chapter": 2, "title": "Secured Cards"}
        ],
        "resources": [
            {"type": "video", "title": "Building Credit From Scratch", "link": "https://www.youtube.com/watch?v=umQeGJKhGY8"},
            {"type": "article", "title": "How to Build Credit Fast", "link": "https://www.nerdwallet.com/article/finance/how-to-build-credit"}
        ],
        "quizzes": [
            {
                "chapter": 3,
                "questions": [
                    {
                        "question": "One way to build credit is by...",
                        "options": ["Not using any credit at all", "Using a secured credit card", "Taking multiple payday loans", "Paying cash only"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Paying your credit card balance in full each month...",
                        "options": ["Hurts your score", "Has no effect", "Helps your credit score", "Triggers extra fees"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "A secured card requires...",
                        "options": ["A co-signer", "A deposit as collateral", "No payments ever", "A high credit score already"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Keeping old credit accounts open...",
                        "options": ["Lowers your score", "Has no impact", "Lengthens your credit history positively", "Deletes credit history"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Credit-building loans are mostly offered by...",
                        "options": ["Gyms", "Banks and credit unions", "Grocery stores", "Airlines"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 4,
        "title": "Fixing Bad Credit",
        "description": "Recover from a poor credit history.",
        "chapters": [
            {"chapter": 1, "title": "Debt Repayment"},
            {"chapter": 2, "title": "Disputing Errors"}
        ],
        "resources": [
            {"type": "article", "title": "How to Fix Bad Credit", "link": "https://www.experian.com/blogs/news/2019/06/improve-credit-score/"},
            {"type": "video", "title": "Fixing Your Credit Score", "link": "https://www.youtube.com/watch?v=ETdEJSRCE1I"}
        ],
        "quizzes": [
            {
                "chapter": 4,
                "questions": [
                    {
                        "question": "To fix bad credit, start by...",
                        "options": ["Ignoring debt collectors", "Repaying debts on time", "Closing all accounts", "Filing for bankruptcy immediately"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Disputing errors on your credit report can...",
                        "options": ["Hurt your score", "Improve your score if errors are removed", "Freeze your credit forever", "Make loans free"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Paying off collections can...",
                        "options": ["Instantly remove them", "Slowly help improve your score", "Hurt your score more", "Cancel your taxes"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Regularly checking your credit report can help catch...",
                        "options": ["Identity theft", "New TV shows", "Traffic violations", "Grocery discounts"],
                        "correctAnswer": 0
                    },
                    {
                        "question": "Debt repayment plans can be created with help from...",
                        "options": ["Friends only", "Certified credit counselors", "Gas station attendants", "Gamers"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 5,
        "title": "Maintaining Good Credit",
        "description": "Keeping your credit strong over time.",
        "chapters": [
            {"chapter": 1, "title": "Monitoring Reports"},
            {"chapter": 2, "title": "Preventing Fraud"}
        ],
        "resources": [
            {"type": "video", "title": "Credit Monitoring Tips", "link": "https://www.youtube.com/watch?v=gQf9c_oW5tw"},
            {"type": "article", "title": "Protect Your Credit", "link": "https://www.consumer.ftc.gov/articles/how-keep-your-personal-information-secure"}
        ],
        "quizzes": [
            {
                "chapter": 5,
                "questions": [
                    {
                        "question": "Monitoring your credit reports helps you...",
                        "options": ["Decrease your income", "Spot errors early", "Get more junk mail", "Lower your phone bill"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Fraud prevention is important because...",
                        "options": ["Fraud boosts your credit", "Identity theft can harm your credit score", "It makes shopping faster", "It reduces your taxes"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Using two-factor authentication protects your...",
                        "options": ["Travel plans", "Credit accounts", "Cooking recipes", "Fitness routines"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "You should check your credit reports at least...",
                        "options": ["Once every 10 years", "Never", "Once a year", "Every week"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "Setting up alerts with banks can help detect...",
                        "options": ["New shopping deals", "Unauthorized transactions", "New movies", "Lottery winnings"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    }
],

    "Smart Banking": [
    {
        "step": 1,
        "title": "Banking Basics",
        "description": "Understand the types of bank accounts and how they work.",
        "chapters": [
            {"chapter": 1, "title": "Checking vs Savings"},
            {"chapter": 2, "title": "Opening an Account"}
        ],
        "resources": [
            {"type": "video", "title": "Bank Accounts Explained", "link": "https://www.youtube.com/watch?v=4v0jMnzIezQ"},
            {"type": "article", "title": "Checking vs. Savings Accounts", "link": "https://www.investopedia.com/articles/banking/09/checking-savings-accounts.asp"}
        ],
        "quizzes": [
            {
                "chapter": 1,
                "questions": [
                    {
                        "question": "A checking account is best used for...",
                        "options": ["Long-term savings", "Daily transactions", "Buying investments", "Paying taxes"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A savings account is mainly for...",
                        "options": ["Everyday spending", "Storing money safely and earning interest", "Paying loans", "Shopping sprees"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Opening a bank account usually requires...",
                        "options": ["Only a phone number", "ID and a minimum deposit", "Owning a business", "A perfect credit score"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Which is usually true about savings accounts?",
                        "options": ["They have lower interest than checking accounts", "They offer no interest", "They help build your credit score", "They typically earn more interest than checking accounts"],
                        "correctAnswer": 3
                    },
                    {
                        "question": "A major benefit of banking is...",
                        "options": ["Losing money", "Keeping cash under your mattress", "Safety and convenience for your money", "Spending without records"],
                        "correctAnswer": 2
                    }
                ]
            }
        ]
    },
    {
        "step": 2,
        "title": "Online Banking",
        "description": "Benefits and safety of online and mobile banking.",
        "chapters": [
            {"chapter": 1, "title": "Mobile Banking Apps"},
            {"chapter": 2, "title": "Online Safety"}
        ],
        "resources": [
            {"type": "article", "title": "Is Online Banking Safe?", "link": "https://www.nerdwallet.com/article/banking/online-banking-safety"},
            {"type": "video", "title": "Online Banking Explained", "link": "https://www.youtube.com/watch?v=YaQ0dwi7A-0"}
        ],
        "quizzes": [
            {
                "chapter": 2,
                "questions": [
                    {
                        "question": "Online banking lets you...",
                        "options": ["Travel for free", "Access your bank accounts digitally", "Avoid paying bills", "Buy houses instantly"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Mobile banking apps allow users to...",
                        "options": ["Only deposit checks", "Manage accounts, pay bills, transfer funds", "Play games", "Order food"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A key safety tip for online banking is...",
                        "options": ["Use public Wi-Fi", "Share your password", "Use two-factor authentication", "Leave accounts logged in"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "A risk of online banking is...",
                        "options": ["Immediate rewards", "Identity theft if not secured", "Better budgeting", "More interest earned"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A common feature of mobile banking is...",
                        "options": ["Live shopping", "Direct deposit setup", "Gambling apps", "Movie streaming"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 3,
        "title": "Managing Your Money",
        "description": "Tips for managing accounts effectively.",
        "chapters": [
            {"chapter": 1, "title": "Reading Bank Statements"},
            {"chapter": 2, "title": "Avoiding Overdrafts"}
        ],
        "resources": [
            {"type": "video", "title": "How to Manage Your Bank Account", "link": "https://www.youtube.com/watch?v=k8Yy33Xprc8"},
            {"type": "article", "title": "How to Avoid Bank Fees", "link": "https://www.investopedia.com/articles/banking/08/avoiding-bank-fees.asp"}
        ],
        "quizzes": [
            {
                "chapter": 3,
                "questions": [
                    {
                        "question": "A bank statement shows...",
                        "options": ["School grades", "Your account activity", "Health records", "Phone usage"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Overdraft happens when you...",
                        "options": ["Deposit too much money", "Withdraw more money than you have", "Save too much", "Earn a bonus"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "To avoid overdraft fees, you can...",
                        "options": ["Turn off overdraft protection", "Ignore your account balance", "Spend without checking", "Always use credit cards"],
                        "correctAnswer": 0
                    },
                    {
                        "question": "Reviewing your transactions helps...",
                        "options": ["Overspend easily", "Spot unauthorized charges", "Earn extra money", "Get more loans"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Setting account alerts can help you...",
                        "options": ["Shop faster", "Track balance changes", "Spend more", "Watch videos"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 4,
        "title": "Understanding Credit Cards",
        "description": "How to use credit cards responsibly.",
        "chapters": [
            {"chapter": 1, "title": "Credit Card Terms"},
            {"chapter": 2, "title": "Interest Rates and Rewards"}
        ],
        "resources": [
            {"type": "video", "title": "Credit Cards for Beginners", "link": "https://www.youtube.com/watch?v=U1xRtyuDdi8"},
            {"type": "article", "title": "Credit Cards Explained", "link": "https://www.nerdwallet.com/article/credit-cards/credit-card-basics"}
        ],
        "quizzes": [
            {
                "chapter": 4,
                "questions": [
                    {
                        "question": "A credit card allows you to...",
                        "options": ["Spend money you already have", "Borrow money up to a limit", "Save for retirement", "Avoid debt forever"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Interest on credit cards is charged when...",
                        "options": ["You pay the full balance", "You carry a balance month to month", "You pay early", "You avoid purchases"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "APR on a credit card stands for...",
                        "options": ["Annual Percentage Rate", "Automated Payment Rate", "Actual Price Rate", "Average Payment Requirement"],
                        "correctAnswer": 0
                    },
                    {
                        "question": "Rewards programs usually offer...",
                        "options": ["Free credit", "Points, cashback, or travel perks", "Increased debt", "Higher APR"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Paying only the minimum amount due each month can lead to...",
                        "options": ["Full debt payoff", "Faster debt accumulation with interest", "Higher credit score", "No credit history"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 5,
        "title": "Protecting Yourself from Fraud",
        "description": "How to protect your banking information.",
        "chapters": [
            {"chapter": 1, "title": "Recognizing Scams"},
            {"chapter": 2, "title": "Using Two-Factor Authentication"}
        ],
        "resources": [
            {"type": "article", "title": "Preventing Bank Fraud", "link": "https://www.consumer.ftc.gov/articles/how-avoid-fraud"},
            {"type": "video", "title": "Fraud Prevention Tips", "link": "https://www.youtube.com/watch?v=Qz5CK_Fl_Fw"}
        ],
        "quizzes": [
            {
                "chapter": 5,
                "questions": [
                    {
                        "question": "Phishing scams often happen through...",
                        "options": ["Phone calls and fake emails", "Grocery stores", "Regular mail only", "ATM machines"],
                        "correctAnswer": 0
                    },
                    {
                        "question": "Two-factor authentication helps protect your...",
                        "options": ["Social media likes", "Bank account access", "Music playlists", "Streaming apps"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A red flag for a scam is...",
                        "options": ["Familiar business names", "Asking for personal info urgently", "Regular bank alerts", "Normal receipts"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "If you notice suspicious activity, you should...",
                        "options": ["Ignore it", "Immediately report to your bank", "Close all your accounts", "Keep spending"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "To protect yourself online, you should...",
                        "options": ["Use weak passwords", "Click random links", "Use secure websites (HTTPS)", "Post your bank info publicly"],
                        "correctAnswer": 2
                    }
                ]
            }
        ]
    }
],
    "Smart Banking": [
    {
        "step": 1,
        "title": "Banking Basics",
        "description": "Understand the types of bank accounts and how they work.",
        "chapters": [
            {"chapter": 1, "title": "Checking vs Savings"},
            {"chapter": 2, "title": "Opening an Account"}
        ],
        "resources": [
            {"type": "video", "title": "Bank Accounts Explained", "link": "https://www.youtube.com/watch?v=4v0jMnzIezQ"},
            {"type": "article", "title": "Checking vs. Savings Accounts", "link": "https://www.investopedia.com/articles/banking/09/checking-savings-accounts.asp"}
        ],
        "quizzes": [
            {
                "chapter": 1,
                "questions": [
                    {
                        "question": "A checking account is best used for...",
                        "options": ["Long-term savings", "Daily transactions", "Buying investments", "Paying taxes"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A savings account is mainly for...",
                        "options": ["Everyday spending", "Storing money safely and earning interest", "Paying loans", "Shopping sprees"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Opening a bank account usually requires...",
                        "options": ["Only a phone number", "ID and a minimum deposit", "Owning a business", "A perfect credit score"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Which is usually true about savings accounts?",
                        "options": ["They have lower interest than checking accounts", "They offer no interest", "They help build your credit score", "They typically earn more interest than checking accounts"],
                        "correctAnswer": 3
                    },
                    {
                        "question": "A major benefit of banking is...",
                        "options": ["Losing money", "Keeping cash under your mattress", "Safety and convenience for your money", "Spending without records"],
                        "correctAnswer": 2
                    }
                ]
            }
        ]
    },
    {
        "step": 2,
        "title": "Online Banking",
        "description": "Benefits and safety of online and mobile banking.",
        "chapters": [
            {"chapter": 1, "title": "Mobile Banking Apps"},
            {"chapter": 2, "title": "Online Safety"}
        ],
        "resources": [
            {"type": "article", "title": "Is Online Banking Safe?", "link": "https://www.nerdwallet.com/article/banking/online-banking-safety"},
            {"type": "video", "title": "Online Banking Explained", "link": "https://www.youtube.com/watch?v=YaQ0dwi7A-0"}
        ],
        "quizzes": [
            {
                "chapter": 2,
                "questions": [
                    {
                        "question": "Online banking lets you...",
                        "options": ["Travel for free", "Access your bank accounts digitally", "Avoid paying bills", "Buy houses instantly"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Mobile banking apps allow users to...",
                        "options": ["Only deposit checks", "Manage accounts, pay bills, transfer funds", "Play games", "Order food"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A key safety tip for online banking is...",
                        "options": ["Use public Wi-Fi", "Share your password", "Use two-factor authentication", "Leave accounts logged in"],
                        "correctAnswer": 2
                    },
                    {
                        "question": "A risk of online banking is...",
                        "options": ["Immediate rewards", "Identity theft if not secured", "Better budgeting", "More interest earned"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A common feature of mobile banking is...",
                        "options": ["Live shopping", "Direct deposit setup", "Gambling apps", "Movie streaming"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 3,
        "title": "Managing Your Money",
        "description": "Tips for managing accounts effectively.",
        "chapters": [
            {"chapter": 1, "title": "Reading Bank Statements"},
            {"chapter": 2, "title": "Avoiding Overdrafts"}
        ],
        "resources": [
            {"type": "video", "title": "How to Manage Your Bank Account", "link": "https://www.youtube.com/watch?v=k8Yy33Xprc8"},
            {"type": "article", "title": "How to Avoid Bank Fees", "link": "https://www.investopedia.com/articles/banking/08/avoiding-bank-fees.asp"}
        ],
        "quizzes": [
            {
                "chapter": 3,
                "questions": [
                    {
                        "question": "A bank statement shows...",
                        "options": ["School grades", "Your account activity", "Health records", "Phone usage"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Overdraft happens when you...",
                        "options": ["Deposit too much money", "Withdraw more money than you have", "Save too much", "Earn a bonus"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "To avoid overdraft fees, you can...",
                        "options": ["Turn off overdraft protection", "Ignore your account balance", "Spend without checking", "Always use credit cards"],
                        "correctAnswer": 0
                    },
                    {
                        "question": "Reviewing your transactions helps...",
                        "options": ["Overspend easily", "Spot unauthorized charges", "Earn extra money", "Get more loans"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Setting account alerts can help you...",
                        "options": ["Shop faster", "Track balance changes", "Spend more", "Watch videos"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 4,
        "title": "Understanding Credit Cards",
        "description": "How to use credit cards responsibly.",
        "chapters": [
            {"chapter": 1, "title": "Credit Card Terms"},
            {"chapter": 2, "title": "Interest Rates and Rewards"}
        ],
        "resources": [
            {"type": "video", "title": "Credit Cards for Beginners", "link": "https://www.youtube.com/watch?v=U1xRtyuDdi8"},
            {"type": "article", "title": "Credit Cards Explained", "link": "https://www.nerdwallet.com/article/credit-cards/credit-card-basics"}
        ],
        "quizzes": [
            {
                "chapter": 4,
                "questions": [
                    {
                        "question": "A credit card allows you to...",
                        "options": ["Spend money you already have", "Borrow money up to a limit", "Save for retirement", "Avoid debt forever"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Interest on credit cards is charged when...",
                        "options": ["You pay the full balance", "You carry a balance month to month", "You pay early", "You avoid purchases"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "APR on a credit card stands for...",
                        "options": ["Annual Percentage Rate", "Automated Payment Rate", "Actual Price Rate", "Average Payment Requirement"],
                        "correctAnswer": 0
                    },
                    {
                        "question": "Rewards programs usually offer...",
                        "options": ["Free credit", "Points, cashback, or travel perks", "Increased debt", "Higher APR"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "Paying only the minimum amount due each month can lead to...",
                        "options": ["Full debt payoff", "Faster debt accumulation with interest", "Higher credit score", "No credit history"],
                        "correctAnswer": 1
                    }
                ]
            }
        ]
    },
    {
        "step": 5,
        "title": "Protecting Yourself from Fraud",
        "description": "How to protect your banking information.",
        "chapters": [
            {"chapter": 1, "title": "Recognizing Scams"},
            {"chapter": 2, "title": "Using Two-Factor Authentication"}
        ],
        "resources": [
            {"type": "article", "title": "Preventing Bank Fraud", "link": "https://www.consumer.ftc.gov/articles/how-avoid-fraud"},
            {"type": "video", "title": "Fraud Prevention Tips", "link": "https://www.youtube.com/watch?v=Qz5CK_Fl_Fw"}
        ],
        "quizzes": [
            {
                "chapter": 5,
                "questions": [
                    {
                        "question": "Phishing scams often happen through...",
                        "options": ["Phone calls and fake emails", "Grocery stores", "Regular mail only", "ATM machines"],
                        "correctAnswer": 0
                    },
                    {
                        "question": "Two-factor authentication helps protect your...",
                        "options": ["Social media likes", "Bank account access", "Music playlists", "Streaming apps"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "A red flag for a scam is...",
                        "options": ["Familiar business names", "Asking for personal info urgently", "Regular bank alerts", "Normal receipts"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "If you notice suspicious activity, you should...",
                        "options": ["Ignore it", "Immediately report to your bank", "Close all your accounts", "Keep spending"],
                        "correctAnswer": 1
                    },
                    {
                        "question": "To protect yourself online, you should...",
                        "options": ["Use weak passwords", "Click random links", "Use secure websites (HTTPS)", "Post your bank info publicly"],
                        "correctAnswer": 2
                    }
                ]
            }
        ]
    }
]
}


@router.post("/generate/{user_id}")
def generate_learning_path(user_id: int, body: PathRequest = Body(...), db: Session = Depends(get_db)):
    user_goal = body.user_goal

    if user_goal not in prebuilt_paths:
        raise HTTPException(400, detail="Invalid topic. Choose one of: " + ", ".join(prebuilt_paths.keys()))
    
    path_json = prebuilt_paths[user_goal]

    # ✅ Fix: convert quizzes --> quiz
    fixed_path = []
    for step in path_json:
        new_step = step.copy()
        if "quizzes" in new_step:
            # Move quizzes (array) to singular "quiz" field
            new_step["quiz"] = []
            for quiz_set in new_step["quizzes"]:
                new_step["quiz"].extend(quiz_set["questions"])  # take questions only
            del new_step["quizzes"]  # remove old
        fixed_path.append(new_step)

    new_path = LearningPath(
        user_id=user_id,
        path_name=f"Custom Path for {user_goal}",
        path_json=fixed_path
    )
    db.add(new_path)
    db.commit()
    db.refresh(new_path)

    return {"message": "Learning path generated!", "path": fixed_path}


@router.get("/my_paths/{user_id}")
def get_my_learning_paths(user_id: int, db: Session = Depends(get_db)):
    paths = db.query(LearningPath).filter(LearningPath.user_id == user_id).all()
    return paths
