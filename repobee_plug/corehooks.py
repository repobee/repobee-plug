"""Hookspecs for repobee core hooks.

Core hooks provide the basic functionality of repobee. These hooks all have
default implementations, but are overridden by any other implementation. All
hooks in this module should have the `firstresult=True` option to the hookspec
to allow for this dynamic override.

.. module:: corehooks
    :synopsis: Hookspecs for repobee core hooks.

.. moduleauthor:: Simon Larsén
"""

from typing import Union, Optional, Iterable, List, Mapping, Callable, Tuple

from repobee_plug.containers import hookspec


class PeerReviewHook:
    """Hook functions related to allocating peer reviews."""

    @hookspec(firstresult=True)
    def generate_review_allocations(
        self,
        master_repo_name: str,
        students: Iterable[str],
        num_reviews: int,
        review_team_name_function: Callable[[str, str], str],
    ) -> Mapping[str, List[str]]:
        """Generate a (peer_review_team -> reviewers) mapping for each student
        repository (i.e. <student>-<master_repo_name>), where len(reviewers) =
        num_reviews.

        review_team_name_function should be used to generate review team names.
        It should be called like:

        .. code-block:: python
            
            review_team_name_function(master_repo_name, student)

        .. important::
                
            There must be strictly more students than reviewers per repo
            (`num_reviews`). Otherwise, allocation is impossible.

        Args:
            master_repo_name: Name of a master repository.
            students: Students for which to generate peer review allocations.
            num_reviews: Amount of reviews each student should perform (and
                consequently amount of reviewers per repo)
            review_team_name_function: A function that takes a master repo name
                as its first argument, and a student username as its second, and
                returns a review team name.
        Returns:
            a (peer_review_team -> reviewers) mapping for each student repository.
        """


class APIHook:
    """Hooks related to platform APIs."""

    @hookspec(firstresult=True)
    def get_api_class(self):
        """Return an API platform class. Must be a subclass of apimeta.API.
        
        Returns:
            An apimeta.API subclass.
        """

    @hookspec(firstresult=True)
    def api_init_requires(self) -> Tuple[str]:
        """Return which of the arguments to apimeta.APISpec.__init__ that the
        given API requires. For example, the GitHubAPI requires all, but the
        GitLabAPI does not require ``user``.

        Returns:
            Names of the required arguments.
        """
