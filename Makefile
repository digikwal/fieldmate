# Makefile for Fieldmate app

.PHONY: help test test-smoke test-export export setup

# Show help for all make targets
help:
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?##' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'
	@echo ""

# Run all tests (pytest)                          ## Run full test suite
test:
	pytest

# Run smoke tests only                            ## Run smoke tests only (basic execution)
test-smoke:
	pytest -m smoke

# Run export-related tests                        ## Run only tests related to export logic
test-export:
	pytest -m export

# Execute Python-based field setup                ## Run setup_custom_fields() (requires active site)
setup:
	bench --site dev.localhost execute fieldmate.setup.custom_fields.setup_custom_fields

# Export all x_fieldmate = 1 fields to JSON       ## Export fields to custom_field/*.json
export:
	bench --site dev.localhost execute fieldmate.setup.export_fieldmate_fields
