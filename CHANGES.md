# Changes Summary

## Date: 2025-01-XX

### Issues Fixed

1. **NumPy Compatibility Issue**
   - **Problem**: NumPy 2.2.6 was incompatible with PyTorch (compiled with NumPy 1.x)
   - **Solution**: 
     - Added `numpy<2` to `requirements.txt`
     - Downgraded NumPy to version 1.26.4
   - **Files Changed**: `requirements.txt`

2. **LangChain Deprecation Warning**
   - **Problem**: `HuggingFaceEmbeddings` from `langchain_community.embeddings` was deprecated
   - **Solution**:
     - Updated import in `app/utils.py` to use `langchain_huggingface`
     - Added `langchain-huggingface` to `requirements.txt`
   - **Files Changed**: `app/utils.py`, `requirements.txt`

3. **Tokenizers Parallelism Warnings**
   - **Problem**: HuggingFace tokenizers showing parallelism warnings when forking processes
   - **Solution**: Set `TOKENIZERS_PARALLELISM=false` environment variable at startup
   - **Files Changed**: `main.py`

4. **Missing Answer Display**
   - **Problem**: The generated answer was extracted but never printed to the console
   - **Solution**: Added answer display section with clear formatting before sources
   - **Files Changed**: `main.py`

### Files Modified

1. **requirements.txt**
   - Added `numpy<2` (pins NumPy to version 1.x for compatibility)
   - Added `langchain-huggingface` (replaces deprecated embeddings import)

2. **app/utils.py**
   - Changed import from `langchain_community.embeddings` to `langchain_huggingface`
   - Line 8: `from langchain_huggingface import HuggingFaceEmbeddings`

3. **main.py**
   - Added `os.environ["TOKENIZERS_PARALLELISM"] = "false"` at startup (line 5)
   - Added answer display section with formatting (lines 27-29)
   - Improved output formatting with separators for better readability

### Testing

All changes tested and verified:
- ✅ Application starts without NumPy errors
- ✅ No deprecation warnings
- ✅ No tokenizer parallelism warnings
- ✅ Answers are now properly displayed to users
- ✅ Sources/citations still display correctly

### Result

The CRAG system now runs cleanly without warnings and properly displays both answers and sources to users.

