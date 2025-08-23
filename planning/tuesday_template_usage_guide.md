# Tuesday Slide Template Usage Guide

## Overview

The `tuesday_slide_template.qmd` provides a standardized structure for creating weekly Tuesday lecture slides in BANA 4080. This template maintains consistency across weeks while providing flexibility for different content areas.

## Template Structure

### 1. YAML Header Configuration
The template includes all standard configuration elements:
- **RevealJS plugins**: appearance, highlight-text, timer
- **Styling**: Consistent CSS and footer branding
- **Background images**: Customizable title slide backgrounds
- **Code execution**: Optional for weeks with live demonstrations

### 2. Slide Flow Pattern
All Tuesday slides follow this proven pedagogical structure:

1. **Welcome & Agenda** (5 min)
2. **Review & Discussion** (10-15 min) 
3. **Main Content Sections** (35-45 min)
4. **Project/Assessment Discussion** (10-15 min)
5. **Wrap-up & Next Steps** (5 min)

## Customization Instructions

### Required Replacements
Replace all placeholders in `[BRACKETS]` with week-specific content:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `[X]` | Week number | `6` |
| `[MAIN_TOPIC]` | Primary subject | `Writing Efficient Python Code` |
| `[SUBTITLE_DESCRIPTION]` | Supporting description | `Control Flow, Iteration, and Functions` |
| `[BACKGROUND_IMAGE]` | Title slide image | `python-code-background.jpg` |
| `[AGENDA_ITEM_X]` | Agenda bullet points | `Control statements for business logic` |

### Content Sections
Customize the main content sections based on your learning objectives:

1. **Main Section Headers**: Use descriptive, student-friendly titles
2. **Business Context**: Always include real-world business applications
3. **Interactive Elements**: Maintain think-pair-share activities for engagement
4. **Code Examples**: Include when demonstrating concepts (optional)

### Timer Integration
The template includes timer functionality for activities:
- **3-minute timers**: Quick discussions and reviews
- **5-minute timers**: Group brainstorming sessions
- **Custom durations**: Adjust based on activity complexity

Update timer IDs to be unique across slides:
```javascript
initializeTimer("uniqueTimerID", seconds, "slide");
```

## Week-Specific Adaptations

### Theory-Heavy Weeks (e.g., Week 1, 6)
- **Reduce code examples** in favor of conceptual explanations
- **Increase discussion time** for abstract concepts
- **Add more business scenarios** to ground theory in practice

### Technical Weeks (e.g., Week 3, 4, 5)
- **Include live coding demonstrations** using `execute: true`
- **Add data loading examples** with real datasets
- **Show before/after comparisons** of data transformations

### Project Weeks (e.g., Week 7, 13, 14)
- **Expand project discussion section** (20-30 minutes)
- **Include milestone reviews** and timeline updates
- **Add peer feedback activities** for collaborative learning

## Consistent Elements to Maintain

### Visual Branding
- **Footer**: Always "BANA 4080"
- **Background colors**: Use `{background="#43464B"}` for section headers
- **CSS styling**: Reference existing `styles.css`

### Pedagogical Features
- **Previous week review**: Connect learning across sessions
- **Interactive activities**: Minimum 2-3 per session
- **Business context**: Every concept tied to business analytics
- **Lab preparation**: Clear connection to Thursday's hands-on work

### Accessibility
- **Slide numbers**: Always enabled for student reference
- **Clear transitions**: Use `. . .` for progressive reveals
- **Reading time**: Allow processing time before advancing
- **Mobile-friendly**: Ensure students can follow on devices

## Quality Checklist

Before using the template, verify:

- [ ] All `[PLACEHOLDERS]` replaced with specific content
- [ ] Timer IDs are unique across slides
- [ ] Images exist in `slides/images/` directory
- [ ] Code examples are tested and error-free
- [ ] Business examples are relevant and current
- [ ] Slide count appropriate for 60-75 minute session
- [ ] Clear learning objectives stated
- [ ] Connection to lab activities explicit

## Common Customizations

### Adding Pop Quizzes
Insert after the review section:
```markdown
## Pop Quiz: [TOPIC] {.smaller}

**Business Scenario:** [SCENARIO_DESCRIPTION]

[MULTIPLE_CHOICE_QUESTIONS]
```

### Including Guest Content
For industry speakers or special topics:
```markdown
# Guest Perspective {background="#43464B"}

## [GUEST_NAME] from [COMPANY]

[GUEST_INTRODUCTION_AND_CONTEXT]
```

### Assessment Preparation
When reviewing for exams or major assignments:
```markdown
## Study Guide Preview

Key concepts for [ASSESSMENT]:
- [CONCEPT_1] - [BUSINESS_APPLICATION]
- [CONCEPT_2] - [BUSINESS_APPLICATION]
```

## File Management

### Naming Convention
- **Template**: `tuesday_slide_template.qmd` (keep in planning/)
- **Weekly slides**: `w[X]_tuesday.qmd` (create in slides/)
- **Rendered output**: `w[X]_tuesday.html` (auto-generated)

### Version Control
- **Draft**: Work in planning/ directory first
- **Review**: Test render before moving to slides/
- **Finalize**: Move completed .qmd to slides/ directory
- **Archive**: Keep planning drafts for future reference

## Technical Notes

### Code Execution
- Set `execute: true` only when including live Python demonstrations
- Test all code examples in isolation before including
- Use `echo: false` for setup code that students don't need to see

### Image Management
- Store all images in `slides/images/`
- Use descriptive filenames for easy reference
- Optimize image sizes for web delivery
- Maintain consistent image styling

### Responsive Design
The template works across devices but consider:
- **Font sizes**: Use `.smaller` class for dense content
- **Column layouts**: Stack appropriately on mobile
- **Timer visibility**: Ensure interactive elements work on tablets

---

*This template supports the creation of engaging, consistent, and pedagogically sound Tuesday lecture slides for BANA 4080.*