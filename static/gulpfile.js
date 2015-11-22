// Gulp
var gulp = require('gulp');
// Gulp Plugins
var concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    sass = require('gulp-sass'),
    livereload = require('gulp-livereload'),
    plumber = require('gulp-plumber'),
    rename = require('gulp-rename'),
    imagemin = require('gulp-imagemin'),
    prefix = require('gulp-autoprefixer');

// Sass Task
gulp.task('sass', function(){
    gulp.src('assests/scss/*.scss')
        .pipe(plumber())
        .pipe(sass())
        .pipe(prefix('last 2 versions'))
        .pipe(gulp.dest('css/'))
        .pipe(sass({ outputStyle: 'compressed' }))
        .pipe(prefix('last 2 versions'))
        .pipe(rename('main.min.css'))
        .pipe(gulp.dest('css/'))
        .pipe(livereload());
});


// Concat and Minify Javascript Files
gulp.task('scripts', function(){
    gulp.src('assests/js/*.js')
    .pipe(plumber())
    .pipe(concat('all.js'))
    .pipe(gulp.dest('js/'))
    .pipe(rename('all.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('js/'))
    .pipe(livereload());
});


// Compress Images
gulp.task('images', function(){
    gulp.src('assests/images/*')
    .pipe(plumber())
    .pipe(imagemin())
    .pipe(gulp.dest('img/'))
    .pipe(livereload());
});


// Reloading HTML
gulp.task('html', function(){
    gulp.src('*.html')
    .pipe(plumber())
    .pipe(livereload());
});


// Watch for tasks
gulp.task('watch', function(){
    var server = livereload({start: true});

    gulp.watch('assests/scss/*.scss', ['sass']);
    gulp.watch('assests/scss/**/*.scss', ['sass']);
    gulp.watch('assests/js/*.js', ['scripts']);
    gulp.watch('assests/images/*', ['images']);
    gulp.watch('*.html', ['html']);
});


// Default Task
gulp.task('default', ['sass', 'scripts', 'images', 'watch']);
