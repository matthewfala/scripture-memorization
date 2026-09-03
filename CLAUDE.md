# CLAUDE.md

## Rules for Agents Writing Documents

Agents writing documents must follow these rules:

1. Whenever modifying a document, you must include a section at the bottom of the document called "## Human Prompts".
2. For the initial session of the document writing, add "#### Initial Document Written {`On` + date or `From` + date range}" followed by a bulleted list of all human entered prompts from the context that resulted in the document.
3. For subsequent modifications to an existing document, add a new section "#### Document Modification {`On` + date or `From` + date range}" followed by a bulleted list of all human entered prompts from the context that resulted in the document's modification.
4. Do not put Claude in the commit messages or list an agent as a co-author in the git commits.

## Rules for Agents Writing Code

Agents writing code must follow these rules when working on this repository:

1. After making your change and adding appropriate tests, build the code, and fix any build and test errors from your change.
2. Create a commit with a short commit message. Follow the commit with two new lines and a short description. Use 50 columns in the description. Add 2 newlines, then the text "Human Prompts:" followed by a bulleted list of all human entered text towards the change.
3. For any followup change that is related to the current change, you must amend the previous commit, updating the message according to the previous rules. Any new human text must be included in the Human Prompts section along with the Human Prompts from the commit that is being amended.
4. Do not put Claude in the commit messages or list an agent as a co-author in the git commits.

## Rules for Agents Following Procedures

The repository's processes are defined by the procedure documents in
`navigators/procedures/` (`PIPELINE.md` is the master map). Agents must
follow these rules:

1. Before doing any pipeline work (extraction, KJV conversion, styles,
   lyrics, song generation, screening, official selection), read the
   relevant procedure document and follow it as written — including its
   file naming conventions and its "what to update, when" obligations.
2. Whenever the process actually followed changes — a new step, a changed
   threshold or convention, a lesson that alters how a step should be done
   next time — update the corresponding procedure document in the same
   session, in the same commit as the change where practical. The
   documents must always match how the work is really done; a process
   change without a matching document update is incomplete work.
3. A new recurring process gets a new numbered procedure document plus a
   `PIPELINE.md` entry; a one-off action does not.
4. Deviating from a procedure requires either the human's approval or an
   update to the procedure itself (rule 2) — never a silent divergence.

## Human Prompts

#### Initial Document Written On 2026-08-27

- Please make a CLAUDE.md at the root repo folder: Agents writing documents must follow these rules 1. Whenever modifying a document, you must include a section at the bottom of the document called "## Human Prompts" 2. For the initial session of the document writting, add "#### Initial Document Written {`On` + date or `From` + date range}" followed by a bulleted list of all human entered prompts from the context that resulted in the document. 3. For subsequent modifications to an existing document, add a new section "#### Document Modification {`On` + date or `From` + date range} followed by a bulleted list of all human entered prompts from the context that resulted in the document's modification. 4. Do not put Claude in the commit messages or list an agent as a co-author in the git commits. Agents writing code must follow these rules when working on this repository. 1. After making your change and adding appropriate tests, build the code, and fix any build and test errors from your change. 2. Create a commit with a short commit message. Follow the commit with two new lines and a short description. Use 50 column in the description. Add 2 newlines, then the text Human Prompts: followed by a bulletted list of all human entered text towards the change. 3. For any followup change that is related to the current change you must ammend the previous commit, updating the message according to the previous rules. Any new human text must be included in the Human Prompts section along with the Human Prompts from the commit that is being ammended. 4. Do not put Claude in the commit messages or list an agent as a co-author in the git commits.

#### Document Modification On 2026-09-02

- Can you modify claude.md so that any time the procedure are changed the corresponding procedure documents are updated. And also to direct to following the procedure.
