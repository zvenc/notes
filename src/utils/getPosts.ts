import type { Post, PostModule } from '../types';

// get all the .md files
export async function getPosts(): Promise<Post[]> {
	const postModules: PostModule = import.meta.glob('../content/posts/*.md');

	// resolve modules and extract frontmatter and content
	const posts = await Promise.all(
		Object.entries(postModules).map(async ([path, resolver]) => {
			const post = await resolver();
			return {
				...post,
				slug: path.split('/').pop().split('.').shift() || '', 
				Content: post.default,
			};
		})
	);

	return posts;
}

