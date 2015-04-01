set(BII_TESTS_WORKING_DIR ${CMAKE_CURRENT_SOURCE_DIR})
# Copying data files to project/bin folder
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/samples")
  file(COPY "${CMAKE_CURRENT_SOURCE_DIR}/samples/monster.fbs"
            "${CMAKE_CURRENT_SOURCE_DIR}/samples/monsterdata.json"
      DESTINATION
            "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/samples")
endif()
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/tests")
  file(COPY "${CMAKE_CURRENT_SOURCE_DIR}/tests"
       DESTINATION
            "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")
endif()

# Actually create targets: EXEcutables and libraries.
ADD_BIICODE_TARGETS()

if(APPLE)
  target_compile_options(${BII_BLOCK_TARGET} INTERFACE -std=c++11 -stdlib=libc++ -Wall -pedantic -Werror -Wextra)
elseif(CMAKE_COMPILER_IS_GNUCXX OR "${CMAKE_CXX_COMPILER_ID}" MATCHES "Clang")
  target_compile_options(${BII_BLOCK_TARGET} INTERFACE -std=c++0x -Wall -pedantic -Werror -Wextra)
endif()

if(FLATBUFFERS_CODE_COVERAGE)
  target_compile_options(${BII_BLOCK_TARGET} INTERFACE -g -fprofile-arcs -ftest-coverage)
  target_compile_options(${BII_BLOCK_TARGET} INTERFACE -fprofile-arcs -ftest-coverage)
endif()

target_include_directories(${BII_BLOCK_TARGET} INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/include)