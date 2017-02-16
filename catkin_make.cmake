# Return a list of all xsd/.xsd files
macro(rs_get_xsds xsdvar)
  file(GLOB _xsd_files RELATIVE "${PROJECT_SOURCE_DIR}/xsd" "${PROJECT_SOURCE_DIR}/xsd/*.xsd")
  set(${xsdvar} "")
  # Loop over each .xsd file, establishing a rule to compile it
  foreach(_xsd ${_xsd_files})
    # Make sure we didn't get a bogus match (e.g., .#Foo.xsd, which Emacs
    # might create as a temporary file).  the file()
    # command doesn't take a regular expression, unfortunately.
    if(${_xsd} MATCHES "^[^\\.].*\\.xsd$")
      list(APPEND ${xsdvar} ${_xsd})
    endif(${_xsd} MATCHES "^[^\\.].*\\.xsd$")
  endforeach(_xsd)
endmacro(rs_get_xsds)

# Generate from xmlschema
macro(xsd2cpp)
  ## get the files
  rs_get_xsds(xsd_files)
  set(_xsd_xsds "")
  set(_xsd_cxxs "")
  
  foreach(_xsd_file ${xsd_files})
    set(_xsd_xsds "xsd/${_xsd_file};${_xsd_xsds}")
    string(REPLACE ".xsd" ".cpp" _xsd_file ${_xsd_file})
    set(_xsd_cxxs "${PROJECT_SOURCE_DIR}/xsd_gen/${PROJECT_NAME}/${_xsd_file};${_xsd_cxxs}")
  endforeach(_xsd_file)
  string(STRIP "${_xsd_cxxs}" _xsd_cxxs)
  string(STRIP "${_xsd_xsds}" _xsd_xsds)
  
  add_custom_command(
    OUTPUT ${_xsd_cxxs}
    COMMAND ${PYTHON_EXECUTABLE} ${asr_xsd2cpp_SOURCE_DIR}/xsd2cpp.py
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    DEPENDS ${_xsd_xsds}
  )

  add_library(${PROJECT_NAME}_asr_xsd2cpp ${_xsd_cxxs})  
  target_link_libraries(${PROJECT_NAME}_asr_xsd2cpp xerces-c)
  
  list(APPEND catkin_LIBRARIES ${PROJECT_NAME}_asr_xsd2cpp)

  include_directories(${PROJECT_SOURCE_DIR}/xsd_gen)
endmacro(xsd2cpp)
