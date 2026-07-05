# GitHub Repository Standards

## Overview
This document outlines the standards and best practices for managing the FPGA Graphing Calculator project on GitHub. Following these guidelines ensures effective collaboration, maintainable code, and professional project presentation.

## 1. Repository Structure

### 1.1 Branch Protection Rules
- **main branch**: Protected; requires pull request reviews and status checks
- **develop branch**: Integration branch; protected; requires pull request reviews
- **feature/* branches**: Developer branches; can be force-pushed but should be rebased regularly
- **release/* branches**: Release preparation; protected; requires approval for merging
- **hotfix/* branches**: Emergency fixes; created from main; merged to both main and develop

### 1.2 Required Branch Protection Settings
For protected branches (main, develop, release/*):
- Require pull request reviews before merging (minimum 1 approving review)
- Dismiss stale approvals when new commits are pushed
- Require status checks to pass before merging
- Require linear history (no merge commits)
- Include administrators
- Restrict who can push to matching branches
- Allow force pushes only for specific roles (maintainers)

### 1.3 Branch Naming Conventions
- `feature/` + JIRA-ID + short-description (e.g., `feature/FPGA-123-floating-point-adder`)
- `bugfix/` + JIRA-ID + short-description (e.g., `bugfix/FPGA-456-fix-hdmi-timing`)
- `hotfix/` + JIRA-ID + short-description (e.g., `hotfix/FPGA-789-fix-boot-loop`)
- `release/` + version-number (e.g., `release/v1.2.0`)
- `docs/` + descriptive-name (e.g., `docs/update-user-guide`)
- `refactor/` + JIRA-ID + short-description (e.g., `refactor/FPGA-321-optimize-parser`)

## 2. Git Workflow

### 2.1 Development Workflow (GitFlow Variant)
1. Developers create feature branches from `develop`
2. Work is committed to feature branches with frequent commits
3. When feature is complete, create pull request from feature branch to `develop`
4. After approval and passing checks, merge using "Squash and merge"
5. Release branches created from `develop` when ready for release
6. Hotfix branches created from `main` for urgent fixes
7. After release, merge release branch to both `main` and `develop`
8. Tag releases on `main` branch with semantic version

### 2.2 Commit Practices
- Make small, focused commits
- Each commit should represent a single logical change
- Commit messages must follow the format in Section 3
- Avoid committing generated files, binaries, or IDE-specific files
- Use `.gitignore` appropriately
- Amend only the most recent commit if needed; avoid rewriting public history

### 2.3 Pull Request Process
1. Ensure branch is up-to-date with target branch (`git fetch origin && git rebase origin/develop`)
2. Run local tests and linters
3. Push branch to remote
4. Create pull request targeting appropriate base branch
5. Fill out pull request template completely
6. Request reviews from appropriate team members
7. Address all review comments
8. Ensure all status checks pass
9. Merge using "Squash and merge" option
10. Delete branch after merge (unless otherwise specified)

## 3. Commit Messages

### 3.1 Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### 3.2 Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect meaning (formatting, missing semicolons, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to build process or auxiliary tools
- `ref`: Reference to external issue or documentation
- `ci`: CI-related changes

### 3.3 Scope
- Optional; indicates module or component affected
- Examples: `fpga-adder`, `sw-parser`, `ui-graph`, `hal-timer`
- Use general scope if affecting multiple areas: `core`, `build`, `doc`

### 3.4 Subject
- Use imperative mood ("add" not "added" or "adding")
- Don't capitalize first letter
- No period at end
- Maximum 50 characters
- Example: `add(floating-point-adder): implement ieee-754 compliant adder`

### 3.5 Body
- Wrap at 72 characters
- Explain what and why, not how
- Use bullet points or numbered lists if needed
- Example:
```
The previous implementation had timing issues on long paths.
This implements a pipelined version with 3 stages to achieve
target frequency of 150MHz.

- Added pipeline registers between stages
- Updated testbench to verify latency
- Adjusted constraints for new timing paths
```

### 3.6 Footer
- Reference issues: `Closes #123` or `Fixes #456`
- Breaking changes: `BREAKING CHANGE: describe the change and migration path`
- Related PRs: `See also #789`

### 3.7 Examples
```
feat(fpga-adder): implement pipelined IEEE 754 single-precision adder

- 3-stage pipeline for 150MHz target frequency
- Handles subnormals, infinity, NaN per IEEE 754-2008
- Flags for overflow, underflow, inexact, invalid operation
- Parameterizable width for future extension

Fixes FPGA-123
```

```
fix(sw-parser): fix buffer overflow in expression parser

- Input validation was missing for long variable names
- Added length check before copying to internal buffer
- Use strncpy instead of strcpy for safety
- Added unit test for boundary conditions

Fixes #456
See also #457 for related issue
```

## 4. Issue Management

### 4.1 Issue Types
Use GitHub Issues with appropriate labels:
- **bug**: Something isn't working
- **feature**: New feature request
- **documentation**: Need for or improvement to documentation
- **question**: Question about the project
- **discussion**: Topic for discussion
- **help wanted**: Maintainers want help with this
- **good first issue**: Good for newcomers

### 4.2 Issue Templates
Use the templates in `.github/ISSUE_TEMPLATE/`:
- **Bug Report**: For reporting reproducible bugs
- **Feature Request**: For suggesting new features
- **Documentation Request**: For requesting documentation improvements

### 4.3 Labeling Standards
#### Priority Labels
- `priority/critical`: Blocks release; must fix immediately
- `priority/high`: Should fix in next release
- `priority/medium`: Normal priority
- `priority/low`: Nice to have

#### Type Labels
- `type/bug`
- `type/feature`
- `type/documentation`
- `type/question`

#### Area Labels
- `area/fpga`
- `area/software`
- `area/ui`
- `area/math`
- `area/build`
- `area/documentation`

#### Status Labels
- `status/to-do`
- `status/in-progress`
- `status/in-review`
- `status/done`

### 4.4 Issue Writing Guidelines
- **Title**: Clear, concise, describes the problem or feature
- **Description**: 
  - Context and background
  - Steps to reproduce (for bugs)
  - Expected vs actual behavior
  - Screenshots or logs if applicable
  - Possible solutions (optional)
- **Acceptance Criteria**: For features, list conditions that must be met
- **Labels**: Apply appropriate labels immediately
- **Assignee**: Assign to responsible party or leave unassigned for triage
- **Milestone**: Associate with appropriate milestone if applicable
- **Projects**: Add to relevant project boards

## 5. Pull Request Standards

### 5.1 PR Description
Use the template in `.github/PULL_REQUEST_TEMPLATE/`:
- **Summary**: Brief description of changes
- **Related Issue**: Closes #XXX or Related to #XXX
- **Type of Change**: Bug fix, feature, documentation, etc.
- **Checklist**: 
  - [ ] Code follows coding standards
  - [ ] Tests added/updated
  - [ ] Documentation updated
  - [ ] No warning during compilation
  - [ ] Verified on target hardware (if applicable)
- **Screenshots/GIFs**: For UI changes
- **Verification**: How changes were tested
- **Notes**: Any additional information

### 5.2 Review Process
- **Reviewers**: Request 1-2 relevant experts
- **Timeline**: Respond to review comments within 1 business day
- **Approval**: Require explicit approval from reviewers
- **Changes Requested**: Address all comments; explain if disagreeing
- **Re-review**: Request re-review after addressing comments
- **Merging**: Only merge after approval and all checks passing

### 5.3 Required Status Checks
Configure branch protection to require:
- **CI Build**: Compilation and basic tests pass
- **Code Scan**: Security and quality checks pass
- **License Check**: No incompatible licenses introduced
- **Documentation Build**: Documentation compiles without errors
- **Size Check**: No abnormally large files added

### 5.4 Squash and Merge
- Use "Squash and merge" for most PRs to maintain clean history
- Keep original PR description in commit message body
- Ensure squashed commit follows commit message conventions
- Only use "Merge commit" for complex merges requiring explicit merge
- Never use "Rebase and merge" as it loses context

## 6. Release Management

### 6.1 Versioning
Use Semantic Versioning (SemVer) v2.0.0:
- Format: `MAJOR.MINOR.PATCH`
- **MAJOR**: Incompatible API changes
- **MINOR**: Backwards-compatible functionality addition
- **PATCH**: Backwards-compatible bug fixes
- Pre-release and build metadata available as needed

### 6.2 Release Process
1. Ensure all features for release are merged to `develop`
2. Create release branch: `git checkout -b release/vX.Y.Z develop`
3. Update version files (if applicable)
4. Run final comprehensive testing
5. Create pull request from release branch to `main` and `develop`
6. After approval, merge to `main` using "Squash and merge"
7. Tag the merge commit: `git tag -a vX.Y.Z -m "Release version X.Y.Z"`
8. Push tags: `git push origin --tags`
9. Merge release branch to `develop`
10. Delete release branch
11. Create GitHub Release from the tag
12. Upload release artifacts (bitstream, binaries, documentation)
13. Publish release notes

### 6.3 Release Notes
- Generated from pull request titles and descriptions
- Grouped by type: Features, Bug Fixes, Documentation, etc.
- Include breaking changes notice if applicable
- List known issues if any
- Acknowledge contributors
- Follow the template in `docs/templates/RELEASE_NOTES_TEMPLATE.md`

### 6.4 Pre-release and Release Candidates
- Use `-rc.N` suffix for release candidates: `v1.2.0-rc.1`
- Use `-preview.N` for preview releases
- Promote to full release when ready
- Remove pre-release identifiers from final version

## 7. Project Management

### 7.1 Milestones
- Align with project phases from PROJECT_PLAN.md
- Named after release versions or sprint goals
- Have clear due dates
- Contain related issues and pull requests
- Progress tracked through GitHub's milestone views

### 7.2 Project Boards
- Use GitHub Projects (Kanban style)
- Columns typically: Backlog, Ready, In Progress, In Review, Done
- Cards represent issues or pull requests
- Automate movement with workflows where possible
- Review during sprint planning and daily standups

### 7.3 Labels for Project Management
In addition to standard labels:
- `sprint/XX`: Indicates sprint assignment
- `epic/epic-name`: Groups related issues
- `estimated/Xh`: Time estimate (use consistently)
- `actual/Xh`: Actual time spent (fill after completion)

## 8. Automation and CI/CD

### 8.1 GitHub Actions Workflows
Maintain workflows in `.github/workflows/`:
- **ci.yml**: Runs on every push and PR; builds, tests, lints
- **nightly.yml**: Runs nightly; longer running tests, static analysis
- **release.yml**: Triggered on tag; builds release artifacts
- **lint.yml**: Runs code quality checks
- **security.yml**: Runs vulnerability scanning
- **documentation.yml**: Builds and validates documentation

### 8.2 Workflow Naming
- Use descriptive names: `CI - Build and Test`, `Nightly - Security Scan`
- Files named descriptively: `ci-build-test.yml`, `nightly-security.yml`

### 8.3 Workflow Permissions
- Use least privilege principle
- Specify required permissions explicitly:
```yaml
permissions:
  contents: read
  pull-requests: write
  issues: write
```

### 8.4 Environment Protection
- Use environment protection rules for deployment workflows
- Require approval for production deployments
- Use environment secrets for sensitive data

## 9. Code Review Guidelines

### 9.1 Reviewer Responsibilities
- Check for adherence to coding standards
- Look for potential bugs, logic errors, or security issues
- Ensure tests are adequate and pass
- Verify documentation is updated if needed
- Check for performance implications
- Confirm that changes are necessary and well-justified
- Ensure proper error handling
- Verify that dependencies are appropriate

### 9.2 Author Responsibilities
- Make changes easy to review (small, focused PRs)
- Respond promptly to comments
- Explain design decisions
- Update code based on feedback
- Maintain professional and constructive tone
- Thank reviewers for their time

### 9.3 Review Checklist
#### Functional Correctness
- [ ] Does the code implement the intended feature/fix?
- [ ] Are edge cases handled?
- [ ] Is error handling appropriate?
- [ ] Does it solve the problem without introducing new issues?

#### Code Quality
- [ ] Does it follow coding standards?
- [ ] Is the code readable and maintainable?
- [ ] Are variable and function names descriptive?
- [ ] Is there unnecessary duplication?
- [ ] Are functions appropriately sized?
- [ ] Are comments useful and up-to-date?

#### Testing
- [ ] Are there unit tests for new/modified functionality?
- [ ] Do existing tests still pass?
- [ ] Are tests meaningful and not just for coverage?
- [ ] Is test isolation maintained?

#### Documentation
- [ ] Is user documentation updated if needed?
- [ ] Is API documentation updated if needed?
- [ ] Are inline comments adequate?
- [ ] Is the changelog/updated if needed?

#### Performance and Resources
- [ ] Are there performance implications?
- [ ] Is resource usage within acceptable bounds?
- [ ] Are there potential scalability issues?
- [ ] Are there any obvious inefficiencies?

#### Security
- [ ] Are there any security vulnerabilities introduced?
- [ ] Is input validation adequate?
- [ ] Are there potential injection points?
- [ ] Is authentication/authorization handled correctly?

### 9.4 Handling Disagreements
- Discuss openly and respectfully
- Seek input from additional experts if needed
- Refer to architectural decisions or standards
- Escalate to technical lead if unresolved
- Document resolved disagreements in issue or PR

## 10. Legal and Compliance

### 10.1 Licensing
- All files must contain appropriate license header
- Use SPDX license identifiers where possible: `SPDX-License-Identifier: MIT`
- Maintain THIRD-PARTY.LICENSES file for dependencies
- Run license checks as part of CI
- Ensure compatibility of all dependencies

### 10.2 Copyright
- Update copyright years as needed
- Use consistent format: `Copyright (c) YYYY-YYYY Company Name`
- For contributions: contributors retain copyright but grant license
- Maintain AUTHORS.md or CONTRIBUTORS.md if required

### 10.3 External Dependencies
- Approve all new dependencies through formal process
- Track versions in lockfiles (package.json, Cargo.lock, etc.)
- Monitor for security vulnerabilities
- Consider license compatibility before adding

## 11. Metrics and Monitoring

### 11.1 Repository Health Metrics
- **Pull Request Cycle Time**: Time from open to merge
- **Issue Resolution Time**: Time from open to close
- **Code Coverage**: Percentage of code covered by tests
- **Technical Debt Ratio**: Ratio of remediation cost to development cost
- **Build Success Rate**: Percentage of successful builds
- **Release Frequency**: How often releases are made

### 11.2 Analytics
- Use GitHub Insights for contribution patterns
- Monitor dependency security alerts
- Track issue labels and milestones for trends
- Review code frequency graphs for activity levels

### 11.3 Reporting
- Generate monthly reports for stakeholders
- Include burndown charts for sprints
- Show defect trends and resolution times
- Highlight team velocity and predictability

## 12. Training and Onboarding

### 12.1 New Contributor Checklist
- [ ] Complete GitHub safety training
- [ ] Read CONTRIBUTING.md and this document
- [ ] Set up development environment per documentation
- [ ] Make first contribution to documentation or good first issue
- [ ] Pair program with experienced team member
- [ ] Review recent pull requests to understand process

### 12.2 Documentation Access
- Keep this document in the repository at `GITHUB_STANDARDS.md`
- Reference in CONTRIBUTING.md
- Include in onboarding materials
- Review and update quarterly

### 12.3 Regular Reviews
- Review these standards during sprint retrospectives
- Update based on team feedback and evolving practices
- Maintain change log of significant updates
- Ensure all team members are aware of changes

---

*These GitHub standards are designed to complement the broader CONTRIBUTING.md and PROJECT_PLAN.md documents. They should be reviewed and updated regularly to reflect the team's evolving practices and GitHub's feature updates.*

*Last Updated: 2025-07-05*