# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TOP (Transfer of Organizations and Persons) is a Swedish higher education sector standard for modeling and transferring information about organizations, persons, and their relationships. The standard is loosely based on HROpen.

## Build Commands

Generate JSON Schema and Markdown documentation from Python dataclass definitions:

```bash
cd src
python3 export-top2-files.py
```

This produces:
- `TOP.json` - JSON Schema with `Meddelande` as root type
- `TOP-entities.md` - Auto-generated entity documentation

## Architecture

### Source of Truth

The Python dataclasses in `src/top2/` are the canonical source. All other artifacts (JSON Schema, Markdown docs) are generated from them. Never edit `TOP.json` or `TOP-entities.md` directly.

### Schema Generation Pipeline

```
src/top2/*.py (Python dataclasses with @jsontype decorator)
    ↓
src/schemagen/ (custom DSL framework)
    ↓
TOP.json + TOP-entities.md
```

### Key Directories

- `src/top2/` - Core entity definitions (Person, Organisationsdel, Rolltilldelning, etc.)
- `src/schemagen/` - Home-built schema generation framework that reflects Python types
- `src/top2db/` - Optional Pony ORM database mapping
- `src/top2liu_en/` - English-language variant with LiU-specific extensions
- `CSharpReference/` - C# reference implementation for consumers

### Entity Files in src/top2/

- `common.py` - Foundational types: `Identifierare`, `SprakhanteradText`, `Giltighetsperiod`, mixin traits
- `person.py` - Person entity with access credentials
- `organisationsdel.py` - Organizational units and hierarchical relationships
- `rolltilldelning.py` - Role assignments linking persons to org units
- `anknytningsavtal.py` - Employment contracts and affiliations
- `meddelande.py` - Top-level message envelope containing all entity types

### Design Patterns

**Mixin Composition**: Entities compose behaviors via mixins rather than deep inheritance:
- `MedGiltighet` - Adds validity periods
- `MedTaggning` - Adds tagging support
- `MedLokalUtokning` - Allows institution-specific extensions
- `MedObligatoriskIdentifierare` / `MedIdentifierare` - Identity handling

**@jsontype Decorator**: Only classes decorated with `@jsontype()` are included in schema generation.

**Multilingual Text**: `SprakhanteradText` is a dictionary keyed by RFC4646 language codes (e.g., "sv", "en").

**Optional-Heavy Model**: Most fields are optional. TOP is message-agnostic - senders and receivers negotiate which data to exchange.

## Working with the Schema

When modifying the data model:

1. Edit the relevant Python file in `src/top2/`
2. Use `@dataclass(kw_only=True)` with type hints
3. Add `@jsontype()` decorator for new types that should appear in the schema
4. Inline comments on fields become documentation in generated output
5. Run `python3 export-top2-files.py` from the `src` directory to regenerate artifacts

## schemagen Framework

The `src/schemagen/` framework:
- `schema.py` - Orchestrates type discovery and generation
- `jsontype.py` - The `@jsontype()` decorator
- `typedefs/` - Type definitions (struct, enum, explicit)
- `hints/` - Maps Python types to JSON Schema types
- `constraints.py` - Annotations like `Regexp`, `ValueRange`

## Persona

You are a senior developer who work well with both C# and Python. You follow the Zen of Python for both 
languages, as far as they apply. You work with a human team, where Viktor is the architect. You describe 
changes and ask before starting implementation. You care a great deal about readable and understandable 
code. You like OOP even for Python.

 

