from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os

# =========================================================================
# Paste text here
# =========================================================================

SHEET_NUMBER = "3"
SHEET_TOPIC = "Wallets, P2P Networks & Propagation"

# (General task - if relevant)
GENERAL_TASK_OBJECTIVE = "Gain practical experience with non-custodial wallets and on-chain tracking."

GENERAL_TASK_STEPS = [
  "a) **Setup**: Create a wallet with a browser extension (e.g., MetaMask, Rabby, or Phantom). Securely write down your Seed Phrase on paper (do not save it digitally).",
  "b) **Faucet**: Switch your wallet to a Testnet (e.g., Ethereum Sepolia or Bitcoin Testnet). Find a 'Faucet' online to claim free test tokens.",
  "c) **Transact**: Send a small amount of test tokens to another address (you can generate a second address yourself or send to a friend).",
  "d) **Verify**: Copy your Transaction ID (TxID) and look it up on a Block Explorer (e.g., Etherscan Sepolia or Mempool.space Testnet)."
]

GENERAL_TASK_DELIVERABLE = "Screenshot of your successful transaction on the Block Explorer (which info can you see?)"

GENERAL_TASK_CHEAT_SHEET = [
  "**1. The Seed Phrase (The Master Key)**\nWhat it is: A list of 12 or 24 random words generated when you create your wallet (e.g., army, vanilla, hero, kitchen...).\nWhy it matters: This is the 'root' of your account. If you lose your password, these words can restore your wallet on any computer.\nSafety Rule: Never type this into a website, save it in a Google Doc, or take a screenshot. If someone sees these words, they own your money.",
  "**2. Testnet (The Sandbox)**\nWhat it is: A clone of the main blockchain used for testing.\nWhy we use it: It works exactly like the real thing (same software, same logic), but the tokens are 'Monopoly Money'-they have zero real-world financial value.\nImportant: Your wallet address looks the same on both Mainnet and Testnet, so always double-check which network you are connected to before sending real funds.",
  "**3. Faucet (The Free Dispenser)**\nWhat it is: A website that gives out free Testnet tokens to developers and students.\nWhy it exists: You need 'Gas' (transaction fees) to do anything on a blockchain. Since you can't buy Testnet tokens on an exchange (because they are worthless), Faucets give them away so you can practice.\nHow to use: Copy your wallet address, paste it into the Faucet website, and click 'Send.'",
  "**4. TxID / Transaction Hash (The Tracking Number)**\nWhat it is: A unique string of characters (e.g., 0x7f9a...) generated the moment you send a transaction.\nAnalogy: It is exactly like a FedEx Tracking Number.\nUsage: If a friend asks, 'Did you pay me?', you don't send a screenshot of your wallet balance; you send them this TxID so they can verify the payment themselves.",
  "**5. Block Explorer (The Public Ledger)**\nWhat it is: A search engine (like Etherscan.io) that reads raw blockchain data and presents it as a readable receipt.\nHow to use: Go to the Explorer (ensure it is the Testnet version, e.g., sepolia.etherscan.io). Paste your TxID into the search bar. You will see the official proof: Status (Success), Timestamp, Fee Paid, and Amount Sent."
]

# GROUP TASKS
GROUP_TASKS = [
  {
    "title": "Group 1: Wallets & Key Management (Custody)",
    "objective": "Categorize storage methods and understand why 'Seed Phrases' are the most critical secret.",
    "research": [
      "a) Taxonomy: Define Hot, Cold, Custodial, Non-Custodial, Hardware, and Paper wallets. Which one connects to the internet? Which one relies on a 3rd party?",
      "b) The 'Master Key' (BIP-39): Research why modern wallets give you 12 English words instead of a random string of code.",
      "c) Address Reuse (Privacy): Compare a Bitcoin Wallet to an Ethereum Wallet. Why does Metamask usually keep the same address forever, while a Bitcoin wallet generates a new address for every transaction?"
    ],
    "actionable": "A Risk Matrix: Compare 5 storage methods (e.g., Ledger, Metamask, Coinbase Mobile App, Paper Wallet, Brain Wallet) across Security, Convenience, and Risk of User Error."
  },
  {
    "title": "Group 2: The Gossip Protocol & Propagation",
    "objective": "How information moves without a central router.",
    "research": [
      "a) Flooding: Research how a transaction propagates via the 'Gossip Protocol.'",
      "b) Latency: What happens if a node in Tokyo sees a block before a node in Munich? (Orphan/Stale blocks).",
      "c) Compact Blocks: How has Bitcoin optimized propagation (e.g., BIP 152)?"
    ],
    "actionable": "A Network Map Visualization: Trace the journey of a transaction from 'Click Send' to 'Mempool of a Chinese Miner,' including the hops between nodes."
  },
  {
    "title": "Group 3: Node Roles & Trust",
    "objective": "Differentiate the actors in the system.",
    "research": [
      "a) The Hierarchy: Define Full Nodes, Pruned Nodes, Light Nodes (SPV), and Mining Nodes.",
      "b) Don't Trust, Verify: Why is running a Full Node considered the only way to be 'sovereign'? What specific rules does a Full Node check?",
      "c) Requirements: What hardware is needed to run a Bitcoin Full Node vs. a Solana Validator today?"
    ],
    "actionable": "A Comparison Chart: 'Node Types.' Columns: Storage Required, Bandwidth, Trust Assumption, Contribution to Network Health."
  },
  {
    "title": "Group 4: Network Security & Attacks",
    "objective": "How the network defends against malicious peers.",
    "research": [
      "a) Sybil Attack: What is it? How does PoW prevent it? (relation to the Byzantine generals problem)",
      "b) Eclipse Attack: How can an attacker isolate a specific node?",
      "c) DDoS: Why is it hard to DDoS the Bitcoin network?"
    ],
    "actionable": "Compare previously happened and possible network attacks, their consequences, and preventive measures."
  }
]

# (optional links
OPTIONAL_LINKS = [
  "- [How Crypto Gets Stolen: Risks to Beware Of](https://www.ledger.com/academy/basic-basics/2-how-to-own-crypto/how-crypto-gets-stolen-risks-to-beware-of)",
  "- [What are Hierarchical Deterministic (HD) Wallets?](https://www.ledger.com/academy/crypto/what-are-hierarchical-deterministic-hd-wallets)",
  "- [BIP-39: The Low-Key Guardian of Your Crypto Freedom](https://www.ledger.com/academy/bip-39-the-low-key-guardian-of-your-crypto-freedom)"
]


# =========================================================================
# actual code (not important)
# =========================================================================

class PDF(FPDF):
  def header(self):
    pass

  def footer(self):
    self.set_y(-20)
    self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
    self.ln(2)
    self.set_font('Times', 'I', 9)

    if self.page_no() == 1:
      self.cell(self.epw / 2, 10, SHEET_TOPIC, align='L', new_x=XPos.RIGHT,
                new_y=YPos.TOP)
    else:
      self.cell(self.epw / 2, 10, '', align='L', new_x=XPos.RIGHT,
                new_y=YPos.TOP)

    self.cell(self.epw / 2, 10, f'Page {self.page_no()} / {{nb}}', align='R',
              new_x=XPos.LMARGIN, new_y=YPos.TOP)


def print_first_page_header(pdf, doc_subtitle):
  pdf.set_font('Times', '', 10)
  logo_path = 'logo.png'
  if os.path.exists(logo_path):
    pdf.image(logo_path, x=pdf.l_margin, y=10, w=20)
  else:
    pdf.set_xy(pdf.l_margin, 10)
    pdf.set_font('Courier', 'B', 10)
    pdf.cell(25, 10, "[LOGO]", border=1, align='C')

  top_y = 10
  block_width = 80
  right_x = pdf.w - pdf.r_margin - block_width
  pdf.set_xy(right_x, top_y)
  pdf.set_font('Times', '', 10)
  pdf.multi_cell(block_width, 5,
                 "Web3 Talents\nBlockchain Fundamentals\nCohort 1", align='R',
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)

  pdf.set_y(35)
  pdf.set_font('Times', 'B', 16)
  pdf.cell(pdf.epw, 10, f'Exercise Sheet {SHEET_NUMBER} - {doc_subtitle}',
           new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
  pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
  pdf.ln(5)


# --- HELPER FUNCTIONS ---
line_height = 5.5


def add_question(pdf, question_text):
  if pdf.get_y() + 20 > pdf.h - pdf.b_margin:
    pdf.add_page()
  pdf.set_font('Times', '', 11)
  safe_text = question_text.replace("’", "'").replace("“", '"').replace("”",
                                                                        '"').replace(
    "—", "-").replace("–", "-")
  pdf.multi_cell(pdf.epw, line_height, safe_text, new_x=XPos.LMARGIN,
                 new_y=YPos.NEXT, markdown=True)
  pdf.ln(1)


def add_section_header(pdf, title, objective):
  pdf.ln(5)
  pdf.set_font('Times', 'B', 14)
  pdf.cell(pdf.epw, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
  if objective:
    pdf.set_font('Times', 'I', 11)
    pdf.multi_cell(pdf.epw, line_height, f"Objective: {objective}",
                   new_x=XPos.LMARGIN, new_y=YPos.NEXT)
  pdf.ln(2)


def add_subheading(pdf, text):
  pdf.ln(2)
  pdf.set_font('Times', 'B', 12)
  pdf.cell(pdf.epw, 6, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
  pdf.ln(1)


# ==========================================
# GENERATE PDF 1: GENERAL TASK
# ==========================================
def create_general_task_pdf():
  pdf = PDF()
  pdf.alias_nb_pages()
  pdf.add_page()
  pdf.set_auto_page_break(auto=True, margin=20)

  print_first_page_header(pdf, 'General Task')

  add_section_header(pdf, "General Task (For Everyone)", GENERAL_TASK_OBJECTIVE)

  add_subheading(pdf, "Task Steps")
  for step in GENERAL_TASK_STEPS:
    add_question(pdf, step)

  add_subheading(pdf, "Deliverable")
  add_question(pdf, GENERAL_TASK_DELIVERABLE)

  if GENERAL_TASK_CHEAT_SHEET:
    add_subheading(pdf, "Cheat Sheet to fulfill general task:")
    for cheat in GENERAL_TASK_CHEAT_SHEET:
      add_question(pdf, cheat)

  filename = f"Sheet_{SHEET_NUMBER}_General_Task.pdf"
  pdf.output(filename)
  print(f"PDF 1 generated successfully: {filename}")


# ==========================================
# GENERATE PDF 2: GROUP TASKS
# ==========================================
def create_group_tasks_pdf():
  pdf = PDF()
  pdf.alias_nb_pages()
  pdf.add_page()
  pdf.set_auto_page_break(auto=True, margin=20)

  print_first_page_header(pdf, 'Group Tasks')

  for group in GROUP_TASKS:
    add_section_header(pdf, group["title"], group["objective"])

    add_subheading(pdf, "Research & Analysis")
    for question in group["research"]:
      add_question(pdf, question)

    add_subheading(pdf, "Actionable Output")
    add_question(pdf, group["actionable"])

  if OPTIONAL_LINKS:
    pdf.ln(10)
    add_section_header(pdf, "Optional Links for Further Reading", "")
    for link in OPTIONAL_LINKS:
      add_question(pdf, link)

  filename = f"Sheet_{SHEET_NUMBER}_Group_Tasks.pdf"
  pdf.output(filename)
  print(f"PDF 2 generated successfully: {filename}")


if __name__ == '__main__':
  create_general_task_pdf()
  create_group_tasks_pdf()